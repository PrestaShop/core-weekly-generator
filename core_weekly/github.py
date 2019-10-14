# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests_cache
import logging
import requests
import ssl
import time

logger = logging.getLogger(__name__)
ssl._create_default_https_context = ssl._create_unverified_context


# Github api
#
class GitHub():
    def __init__(self, no_cache, debug):
        self.sleep_time = 2
        self.url = 'https://api.github.com/search/issues?per_page=100'
        self.no_cache = no_cache
        self.is_debug = debug

        if not self.no_cache:
            requests_cache.install_cache('cache')

    ##
    # Build github query
    #
    # :param query String
    #
    def build_query(self, query):
        return '&q=org:PrestaShop+is:public+-repo:prestashop/prestashop.github.io+' + query

    ##
    # Generate github request and return json content
    #
    # :param str query: Represents a GitHub query
    # :param bool is_issue: Is issue or pull request
    #
    def get_json(self, query, is_issue=True):
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

    ##
    # Execute
    #
    def execute(self, request_url):
        logger.debug(
            'URL: ' + request_url
        )

        resp = requests.get(
            request_url
        )

        data = resp.json()

        if hasattr(resp, 'from_cache') and not resp.from_cache:
            time.sleep(self.sleep_time)

        if 'next' in resp.links:
            data += self.execute(
                resp.links['next']['url']
            )

        return data
