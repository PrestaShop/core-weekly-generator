#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from coreteam import CORE_TEAM
from coreteam import PROJECTS
from coreteam import CATEGORIES
from collections import OrderedDict
from pprint import pprint

import os
import sys
import json
import time
import re
import ssl


ssl._create_default_https_context = ssl._create_unverified_context

# Just in case it's not python 2
try:
    import urllib.request as urlrequest
except ImportError:
    import urllib as urlrequest


##
# Github api
#
class GitHub():
    def __init__(self):
        self.sleep_time = 2
        self.url = 'https://api.github.com/search/issues?per_page=100'

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
        
        # debug only
        #print(
        #    'Processing request for query: {query_type}+{query}'.format(
        #        query=query,
        #        query_type=query_type
        #    )
        #)
        
        filename = '{query}-{query_type}'.format(
            query=query,
            query_type=query_type
        )

        if os.path.exists('./' + filename):
            with open(filename, 'r') as f:
                data = f.read()
        else:
            data = urlrequest.urlopen(
                self.url +
                self.build_query(query) +
                '+' +
                query_type
            ).read().decode('utf-8')

            with open(filename, 'w') as f:
                f.write(data)
            time.sleep(self.sleep_time)

        return json.loads(data)


class CoreWeekly():
    def __init__(self, date_range):
        self.github = GitHub()
        self.template = Template()
        self.date_range = date_range

    ##
    # Get opened issues
    #
    def get_opened_issues(self):
        return self.github.get_json(
            'created:{date_range}'.format(date_range=self.date_range)
        )

    ##
    # Get closed issues
    #
    def get_closed_issues(self):
        return self.github.get_json(
            'closed:{date_range}'.format(date_range=self.date_range)
        )

    ##
    # Get fixed issues
    #
    def get_fixed_issues(self):
        return self.github.get_json(
            'label:fixed+closed:{date_range}'.format(date_range=self.date_range)
        )

    ##
    # Get opened pull requests
    #
    def get_opened_pr(self):
        return self.github.get_json(
            'created:{date_range}'.format(date_range=self.date_range),
            False
        )

    ##
    # Get closed pull requests
    #
    def get_closed_pr(self):
        return self.github.get_json(
            'closed:{date_range}'.format(date_range=self.date_range),
            False
        )

    ##
    # Get merged pull request
    #
    def get_merged_pr(self):
        return self.github.get_json(
            'merged:{date_range}'.format(date_range=self.date_range),
            False
        )

    ##
    # Generate Core weekly markdown content
    #
    def generate(self):
        opened_issues = self.get_opened_issues()
        closed_issues = self.get_closed_issues()
        fixed_issues = self.get_fixed_issues()
        opened_pr = self.get_opened_pr()
        closed_pr = self.get_closed_pr()
        merged_pr = self.get_merged_pr()

        content = self.template.headers()
        
        # debug only
        #content += self.template.opened_issues(opened_issues)
        #content += self.template.closed_issues(closed_issues)
        #content += self.template.fixed_issues(fixed_issues)
        #content += ''
        #content += self.template.opened_pr(opened_pr)
        #content += self.template.closed_pr(closed_pr)
        #content += self.template.merged_pr(merged_pr)
        #content += ''
        #content += "\n\n"
        
        content += self.template.issues_links(opened_issues, closed_issues, fixed_issues, self.date_range)
        content += self.template.pr_links(opened_issues, closed_issues, fixed_issues, self.date_range)
        content += self.template.build_merged_pull_requests(merged_pr)

        content += self.template.build_contributors_list(merged_pr)
        content += self.template.footers()

        return content


class Template():
    def __init__(self):
        pass

    ##
    # Default headers
    #
    def headers(self):
        return '''---
layout: post
title:  "PrestaShop Core Weekly - Week XXXX of 2019"
subtitle: "An inside look at the PrestaShop codebase"
date:   XXXX
authors: [ PrestaShop ]
image: /assets/images/2017/04/core_weekly_banner.jpg
icon: icon-calendar
tags:
 - core-weekly
---

This edition of the Core Weekly report highlights changes in PrestaShop\'s core codebase from XXXX to XXXX.

![Core Weekly banner](/assets/images/2018/12/banner-core-weekly.jpg)

## General messages

[XXXX]


## A quick update about PrestaShop\'s GitHub issues and pull requests:
'''

    ##
    # Default footers
    #
    def footers(self):
        return '''
Thank you to the contributors whose PRs haven't been merged yet! And of course, a big thank you to all those who contribute with issues and comments [on GitHub](https://github.com/PrestaShop/PrestaShop)!

If you want to contribute to PrestaShop with code, please read these pages first:

 * [Contributing code to PrestaShop](https://devdocs.prestashop.com/1.7/contribute/contribution-guidelines/)
 * [Coding standards](https://devdocs.prestashop.com/1.7/development/coding-standards/)

...and if you do not know how to fix an issue but wish to report it, please read this: [How to use GitHub to report an issue](https://devdocs.prestashop.com/1.7/contribute/contribute-reporting-issues/). Thank you!

Happy contributin' everyone!
'''

    ##
    # Get opened issues count and status
    #
    def opened_issues(self, result):
        return 'Open issues: {opened_issues_count}, Incomplete results: {query_incomplete_results}'.format(
            opened_issues_count=result['total_count'],
            query_incomplete_results=result['incomplete_results']
        )

    ##
    # Get closed issues count and status
    #
    def closed_issues(self, result):
        return 'Closed issues: {closed_issues_count}, Incomplete results: {query_incomplete_results}'.format(
            closed_issues_count=result['total_count'],
            query_incomplete_results=result['incomplete_results']
        )

    ##
    # Get fixed issues count and status
    #
    def fixed_issues(self, result):
        return 'Fixed issues: {fixed_issues_count}, Incomplete results: {query_incomplete_results}'.format(
            fixed_issues_count=result['total_count'],
            query_incomplete_results=result['incomplete_results']
        )

    ##
    # Get opened pull requests count and status
    #
    def opened_pr(self, result):
        return 'Opened pull requests: {opened_pr_count}, Incomplete results: {query_incomplete_results}'.format(
            opened_pr_count=result['total_count'],
            query_incomplete_results=result['incomplete_results']
        )

    ##
    # Get closed pull requests count and status
    #
    def closed_pr(self, result):
        return 'Closed pull requests: {closed_pr_count}, Incomplete results: {query_incomplete_results}'.format(
            closed_pr_count=result['total_count'],
            query_incomplete_results=result['incomplete_results']
        )

    ##
    # Get merged pull requests count and status
    #
    def merged_pr(self, result):
        return 'Merged pull requests: {merged_pr_count}, Incomplete results: {query_incomplete_results}'.format(
            merged_pr_count=result['total_count'],
            query_incomplete_results=result['incomplete_results']
        )

    ##
    # Get Issues links
    #
    def issues_links(self, opened_issues, closed_issues, fixed_issues, date_range):
        return '''
- [{opened_issues_count} new issues](https://github.com/search?q=org%3APrestaShop+is%3Apublic++-repo%3Aprestashop%2Fprestashop.github.io++is%3Aissue+created%3A{date_range}) have been created in the project repositories;
- [{closed_issues_count} issues have been closed](https://github.com/search?q=org%3APrestaShop+is%3Apublic++-repo%3Aprestashop%2Fprestashop.github.io++is%3Aissue+closed%3A{date_range}), including [{fixed_issues_count} fixed issues](https://github.com/search?q=org%3APrestaShop+is%3Apublic++-repo%3Aprestashop%2Fprestashop.github.io++is%3Aissue+label%3Afixed+closed%3A{date_range}) on the core;
        '''.format(
            opened_issues_count=opened_issues['total_count'],
            closed_issues_count=closed_issues['total_count'],
            fixed_issues_count=fixed_issues['total_count'],
            date_range=date_range
        )

    ##
    # Get Pull requests links
    #
    def pr_links(self, opened_pr, closed_pr, merged_pr, date_range):
        return '''
- [{opened_pr_count} pull requests have been opened](https://github.com/search?q=org%3APrestaShop+is%3Apublic++-repo%3Aprestashop%2Fprestashop.github.io++is%3Apr+created%3A{date_range}) in the project repositories;
- [{closed_pr_count} pull requests have been closed](https://github.com/search?q=org%3APrestaShop+is%3Apublic++-repo%3Aprestashop%2Fprestashop.github.io++is%3Apr+closed%3A{date_range}), including [{merged_pr_count} merged pull requests](https://github.com/search?q=org%3APrestaShop+is%3Apublic++-repo%3Aprestashop%2Fprestashop.github.io++is%3Apr+merged%3A{date_range}).
----------
        '''.format(
            opened_pr_count=opened_pr['total_count'],
            closed_pr_count=closed_pr['total_count'],
            merged_pr_count=merged_pr['total_count'],
            date_range=date_range
        )

    ##
    # Just check if user who create PR is in Core team
    # And change message if not.
    #
    # :param dict user: User information
    #
    def thanks(self, user):
        if user['login'] in CORE_TEAM:
            message = ', by [@{author_name}]({author_url})'
        else:
            message = '. Thank you [@{author_name}]({author_url})'

        return message.format(
            author_name=user['login'],
            author_url=user['html_url'],
        )

    ##
    # Extract core category
    #
    # :param str body: Body string
    #
    def extract_core_category(self, body):
        if (body.find("| WS\r\n") != -1):
            return "WS"
        if (body.find("| FO\r\n") != -1):
            return "FO"
        if (body.find("| BO\r\n") != -1):
            return "BO"
        if (body.find("| IN\r\n") != -1):
            return "IN"
        if (body.find("| TE\r\n") != -1):
            return "TE"
        if (body.find("| CO\r\n") != -1):
            return "CO"

        return 'Misc'

    ##
    # Extract branch
    #
    # :param str body: Body string
    #
    # @todo: improve to remove hardcoded branches
    #
    def extract_branch(self, body):
        if (body.find("1.7.6.x\r\n") != -1):
            return "1.7.6.x"
        if (body.find("1.7.5.x\r\n") != -1):
            return "1.7.5.x"
        if (body.find("develop\r\n") != -1):
            return "develop"

        return 'unknown branch'

    ##
    # Extract repository
    #
    # :param str url: URL string
    #
    def extract_repository(self, url):
        m = re.search('github.com/PrestaShop/(.+?)/', url)
        if m:
            if m.group(1) in PROJECTS.keys():
                # map repository with a project name
                return PROJECTS[m.group(1)]
            
            return m.group(1)

        return url

    ##
    # Sort core items by branch following given branch order
    #
    # thanks https://stackoverflow.com/questions/12031482/custom-sorting-python-dictionary
    #
    def custom_sort(self, dict1 , key_order):

        only_useful_keys = []
        for key in key_order:
            if key in dict1.keys():
                only_useful_keys.append(key)

        items = [dict1[k] if k in dict1.keys() else 0 for k in only_useful_keys] 
        sorted_dict = OrderedDict()

        for i in range(len(only_useful_keys)):
            sorted_dict[only_useful_keys[i]] = items[i]

        return sorted_dict

    ##
    # Build merged pull requests
    #
    # :param dict result: Pull requests
    #
    def build_merged_pull_requests(self, result):
        content = ''

        sorted_results = self.get_repositories(result['items'])
        core_items = sorted_results.get('PrestaShop')
        grouped_core_items = self.sort_core_repositories(core_items)

        # @todo: remove hardcoded branches
        branch_order = ['develop', '1.7.6.x', '1.7.5.x', '1.7.4.x']
        sorted_core_items = self.custom_sort(grouped_core_items, branch_order)

        category_order = ['CO', 'BO', 'FO', 'IN', 'WS', 'TE', 'ME', 'Misc']

        for branch, category_items in sorted_core_items.items():
            content += "\n\n## Code changes in the '"+branch+"' branch (for vXXXX)"

            sorted_category_items = self.custom_sort(category_items, category_order)

            for category, items in sorted_category_items.items():

                if category in CATEGORIES.keys():
                # map category ID with a proper name
                    category_name = CATEGORIES[category]
                else:
                    category_name = category

                content += "\n\n### " + category_name
                for item in items:
                    line = '* [#{pr_number}]({pr_url}): {pr_title}{thanks}'.format(
                        pr_number=item['number'],
                        pr_url=item['html_url'],
                        pr_title=item['title'],
                        thanks=self.thanks(item['user'])
                    )

                    content += "\n\n" + line

        del sorted_results['PrestaShop']

        content +="\n\n" +'## Code changes in modules, themes & tools'

        for repository, items in sorted_results.items():
            content += "\n\n### " + repository
            for item in items:
                line = '* [#{pr_number}]({pr_url}): {pr_title}{thanks}'.format(
                    pr_number=item['number'],
                    pr_url=item['html_url'],
                    pr_title=item['title'],
                    thanks=self.thanks(item['user']),
                )

                content += "\n\n" + line

        return content

    def build_contributors_list(self, result):
        head = '''

<hr />

'''
        thanks = 'Thank you to the contributors whose pull requests were merged since the last Core Weekly Report: '

        contributors = self.get_authors(result['items'])

        return head + thanks + '@' + ', @'.join(contributors) + "!\n"

    ##
    # Get Repositories
    #
    # :param dict items: Repositories
    #
    def get_repositories(self, items):
        results = {}
        for item in items:
            repository = self.extract_repository(item['html_url'])

            if repository in results:
                results[repository].append(item)
            else:
                results.update({repository: []})
                results[repository].append(item)

        return results

    ##
    # Get Authors
    #
    # :param dict items: Repositories
    #
    def get_authors(self, items):
        authors = []
        for item in items:
            author = self.extract_repository(item['user']['login'])
            authors.append(author)

        return list(dict.fromkeys(authors))

    ##
    # Get PrestaShop repositories
    #
    # :param dict items: Repositories
    #
    def sort_core_repositories(self, items):
        sorted_core_items = {}
        for item in items:
            category = self.extract_core_category(item['body'])
            branch = self.extract_branch(item['body'])

            if branch not in sorted_core_items:
                sorted_core_items.update({branch: {}})

            if category not in sorted_core_items[branch]:
                sorted_core_items[branch].update({category: []})

            sorted_core_items[branch][category].append(item)

        return sorted_core_items


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise ValueError('Missing parameters.')

    core_weekly = CoreWeekly(sys.argv[1])
    print(core_weekly.generate())
