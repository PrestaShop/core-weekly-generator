# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from github import Github
from github import UnknownObjectException
import requests_cache
import logging
import requests
import ssl
import time
from datetime import date, datetime, timedelta

logger = logging.getLogger(__name__)
ssl._create_default_https_context = ssl._create_unverified_context


# Github API Client
#
class GitHubClient():
    retries = 0

    def __init__(self, no_cache, debug, github_access_token):
        """Constructor

        :param no_cache: Disable cache
        :type no_cache: bool
        :param debug: Is debug mode enabled
        :type debug: bool
        :param github_access_token: GitHub Access Token
        :type github_access_token: str

        """
        self.sleep_time = 3
        self.url = 'https://api.github.com/search/issues?per_page=100'
        self.no_cache = no_cache
        self.is_debug = debug
        self.github_access_token = github_access_token

        if not self.no_cache:
            requests_cache.install_cache('cache')

    def get_last_week_git_releases(self):
        """Get last week GitRelease objects (see https://pygithub.readthedocs.io/)

        :returns: List of dictionaries <GitRelease, Repository>
        :rtype: list

        """
        g = Github(self.github_access_token)

        all_repositories = g.search_repositories(query="org:PrestaShop")
        last_week_releases = []
        one_week_ago_date = date.today() - timedelta(days=7)
        one_week_ago_datetime = datetime.combine(one_week_ago_date, datetime.min.time())

        for repo in all_repositories:
            try:
                release = repo.get_latest_release()
                if release.published_at > one_week_ago_datetime:
                    last_week_releases.append({'release':release,'repo':repo})

            except UnknownObjectException:
                pass

        return last_week_releases      

    def build_query(self, query):
        """Build GitHub query

        :param query: Query to execute through the API
        :returns: Url which will be executed
        :rtype: str

        """
        return '&q=org:PrestaShop+is:public+-repo:prestashop/prestashop.github.io+' + query

    def get_json(self, query, is_issue=True):
        """Generate GitHub request and return json content

        :param query: Query to execute
        :type query: str
        :param is_issue: Defined if it's an issue or a pull request
        :param is_issue: bool
        :returns: The json content
        :rtype: dict

        """
        query_type = ('is:issue' if is_issue else 'is:pr')

        logger.debug(
            'Processing request for query: {query_type}+{query}'.format(
                query=query,
                query_type=query_type
            )
        )

        data = self.execute(
            self.url + self.build_query(query) + '+' + query_type
        )

        return data

    def execute(self, request_url):
        """Execute url

        :param request_url: The url to execute
        :returns: The HTTP Response
        :rtype: dict

        """
        logger.debug(
            'Execute URL: ' + request_url
        )

        resp = requests.get(
            request_url
        )

        data = resp.json()

        if resp.status_code != 200:
            # Something went wrong, retry
            time.sleep(self.sleep_time)
            GitHub.retries += 1
            if GitHub.retries >= 10:
                raise requests.HTTPError(resp.text)

            return self.execute(request_url)
        else:
            GitHubClient.retries = 0
            # Data not in cache, we must wait because of GitHub API rate limits
            if not hasattr(resp, 'from_cache') or not resp.from_cache:
                time.sleep(self.sleep_time)

            if 'next' in resp.links:
                # Compute items if there is a next url
                data['items'] += self.execute(
                    resp.links['next']['url']
                )['items']
        return data
