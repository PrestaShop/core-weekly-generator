# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from coreteam import CORE_BRANCHES
from coreteam import CORE_TEAM
from coreteam import CATEGORIES
from coreteam import CATEGORIES_REJECT_LIST
from coreteam import BOT_USERS
from collections import OrderedDict
from datetime import date


class Template():
    def __init__(self, parser):
        """Constructor

        :param parser: Parser
        :type parser: core_weekly.Parser
        """
        self.parser = parser

    def headers(self, from_day_to_day_statement, week, year):
        """Default header

        :returns: Original headers
        :rtype: str

        """

        today = str(date.today())

        template = '''---
layout: post
title:  "PrestaShop Core Weekly - Week {week} of {year}"
subtitle: "An inside look at the PrestaShop codebase"
date:   {today}
authors: [ PrestaShop ]
image: /assets/images/2017/04/core_weekly_banner.jpg
twitter_image: /assets/images/theme/banner-core-weekly.jpg
icon: icon-calendar
tags:
 - core-weekly
---

This edition of the Core Weekly report highlights changes in PrestaShop\'s core codebase {from_day_to_day_statement}.

![Core Weekly banner](/assets/images/2018/12/banner-core-weekly.jpg)

## General messages

[write a nice message here, or remove the "General messages" section]


## A quick update about PrestaShop\'s GitHub issues and pull requests:
'''

        return template.format(
            today=today,
            week=str(week),
            year=str(year),
            from_day_to_day_statement=from_day_to_day_statement
        )

    def footers(self):
        """Default footer

        :returns: Original footer
        :rtype: str

        """
        return '''
Thank you to the contributors whose PRs haven't been merged yet! And of course, a big thank you to all those who contribute with issues and comments [on GitHub](https://github.com/PrestaShop/PrestaShop)!

If you want to contribute to PrestaShop with code, please read these pages first:

 * [Contributing code to PrestaShop](https://devdocs.prestashop.com/1.7/contribute/contribution-guidelines/)
 * [Coding standards](https://devdocs.prestashop.com/1.7/development/coding-standards/)

...and if you do not know how to fix an issue but wish to report it, please read this: [How to use GitHub to report an issue](https://devdocs.prestashop.com/1.7/contribute/contribute-reporting-issues/). Thank you!

Happy contributin' everyone!
'''

    def opened_issues(self, result):
        """Get opened issues count and status

        :param result: GitHub response
        :returns: Issues information
        :rtype: str

        """
        return 'Open issues: {opened_issues_count}, Incomplete results: {query_incomplete_results}'.format(
            opened_issues_count=result['total_count'],
            query_incomplete_results=result['incomplete_results']
        )

    def closed_issues(self, result):
        """Get closed issues count and status

        :param result: GitHub response
        :returns: Issues information
        :rtype: str

        """
        return 'Closed issues: {closed_issues_count}, Incomplete results: {query_incomplete_results}'.format(
            closed_issues_count=result['total_count'],
            query_incomplete_results=result['incomplete_results']
        )

    def fixed_issues(self, result):
        """Get fixed issues count and status

        :param result: GitHub response
        :returns: Issues information
        :rtype: str

        """
        return 'Fixed issues: {fixed_issues_count}, Incomplete results: {query_incomplete_results}'.format(
            fixed_issues_count=result['total_count'],
            query_incomplete_results=result['incomplete_results']
        )

    def opened_pull_requests(self, result):
        """Get opened pull requests count and status

        :param result: GitHub response
        :returns: Pull requests information
        :rtype: str

        """
        return 'Opened pull requests: {opened_pull_requests_count}, Incomplete results: {query_incomplete_results}'.format(
            opened_pull_requests_count=result['total_count'],
            query_incomplete_results=result['incomplete_results']
        )

    def closed_pull_requests(self, result):
        """Get closed pull requests count and status

        :param result: GitHub response
        :returns: Pull requests information
        :rtype: str

        """
        return 'Closed pull requests: {closed_pull_requests_count}, Incomplete results: {query_incomplete_results}'.format(
            closed_pull_requests_count=result['total_count'],
            query_incomplete_results=result['incomplete_results']
        )

    def merged_pull_requests(self, result):
        """Get merged pull requests count and status

        :param result: GitHub response
        :returns: Pull requests information
        :rtype: str

        """
        return 'Merged pull requests: {merged_pull_requests_count}, Incomplete results: {query_incomplete_results}'.format(
            merged_pull_requests_count=result['total_count'],
            query_incomplete_results=result['incomplete_results']
        )

    def issues_links(
            self,
            opened_issues,
            closed_issues,
            fixed_issues,
            date_range
    ):
        """Issues links

        :param opened_issues: GitHub response
        :type opened_issues: dict
        :param closed_issues: GitHub response
        :type closed_issues: dict
        :param fixed_issues: GitHub response
        :type fixed_issues: dict
        :param date_range: Date range used
        :type date_range: str
        :returns: Links for issues
        :rtype: str

        """
        return '''
- [{opened_issues_count} new issues](https://github.com/search?q=org%3APrestaShop+is%3Apublic++-repo%3Aprestashop%2Fprestashop.github.io++is%3Aissue+created%3A{date_range}) have been created in the project repositories;
- [{closed_issues_count} issues have been closed](https://github.com/search?q=org%3APrestaShop+is%3Apublic++-repo%3Aprestashop%2Fprestashop.github.io++is%3Aissue+closed%3A{date_range}), including [{fixed_issues_count} fixed issues](https://github.com/search?q=org%3APrestaShop+is%3Apublic++-repo%3Aprestashop%2Fprestashop.github.io++is%3Aissue+label%3Afixed+closed%3A{date_range}) on the core;
'''.format(
            opened_issues_count=opened_issues['total_count'],
            closed_issues_count=closed_issues['total_count'],
            fixed_issues_count=fixed_issues['total_count'],
            date_range=date_range
        )

    def pull_request_links(
            self,
            opened_pull_requests,
            closed_pull_requests,
            merged_pull_requests,
            date_range
    ):
        """Pull requests links

        :param opened_pull_requests: GitHub Response
        :type opened_pull_requests: dict
        :param closed_pull_requests: GitHub Response
        :type closed_pull_requests: dict
        :param merged_pull_requests: GitHub Response
        :type merged_pull_requests: dict
        :param date_range: Date range used
        :type date_range: str
        :returns: Link for pull requests
        :rtype: str

        """
        return '''- [{opened_pull_requests_count} pull requests have been opened](https://github.com/search?q=org%3APrestaShop+is%3Apublic++-repo%3Aprestashop%2Fprestashop.github.io++is%3Apr+created%3A{date_range}) in the project repositories;
- [{closed_pull_requests_count} pull requests have been closed](https://github.com/search?q=org%3APrestaShop+is%3Apublic++-repo%3Aprestashop%2Fprestashop.github.io++is%3Apr+closed%3A{date_range}), including [{merged_pull_requests_count} merged pull requests](https://github.com/search?q=org%3APrestaShop+is%3Apublic++-repo%3Aprestashop%2Fprestashop.github.io++is%3Apr+merged%3A{date_range}).
        '''.format(
            opened_pull_requests_count=opened_pull_requests['total_count'],
            closed_pull_requests_count=closed_pull_requests['total_count'],
            merged_pull_requests_count=merged_pull_requests['total_count'],
            date_range=date_range
        )

    def thanks(self, user):
        """Check if the user who created the pull request
        is being part of the Core Team, and add a
        Thanks you if not :)

        :param user: User information
        :type user: dict
        :returns: Author line with a thanks you
        :rtype: str

        """
        if user['login'] in CORE_TEAM:
            message = ', by '
        elif user['login'] in BOT_USERS:
            message = '. Built by '
        else:
            message = '. Thank you '

        return message + self.author_line(
            author_name=user['login'],
            author_url=user['html_url'],
        )

    def author_line(self, author_name, author_url, **kwargs):
        """Generate author markdown links

        :param author_name: Author name
        :type author_name: str
        :param author_url: Author profile url
        :type author_url: str
        :returns: Link in markdown to a user profile
        :rtype: str

        """
        return '[@{author_name}]({author_url})'.format(
            author_name=author_name,
            author_url=author_url,
        )

    def custom_sort(self, data, key_order):
        """Sort core items by branch following given branch order
        Thanks https://stackoverflow.com/questions/12031482/custom-sorting-python-dictionary

        :param data: Data we want to sort
        :type data: dict
        :param key_order: Key to order
        :type key_order: str
        :returns: Sorted dict
        :rtype: dict

        """
        only_useful_keys = []
        for key in key_order:
            if key in data.keys():
                only_useful_keys.append(key)

        items = [data[k] if k in data.keys() else 0 for k in only_useful_keys]
        sorted_dict = OrderedDict()

        for i in range(len(only_useful_keys)):
            sorted_dict[only_useful_keys[i]] = items[i]

        return sorted_dict


    def verify_no_unknown_branch(self, grouped_data_by_branches, branches):
        """Verify there is no unknown branch

        :param grouped_data_by_branches: Data we want to verify
        :type grouped_data_by_branches: dict
        :param branches: Core known branches
        :type branches: str
        """
        only_useful_keys = []
        for key in grouped_data_by_branches:
            if key not in branches:
                raise Exception('Cannot find branch '+key+' in configured branches')


    def build_merged_pull_requests(self, result):
        """Build merged pull requests

        :param result: GitHub Response
        :type result: dict
        :returns: Pull requests information
        :rtype: str

        """
        content = ''

        sorted_results = self.get_repositories(result['items'])
        core_items = sorted_results.get('PrestaShop')

        if (core_items is None):
            return ''

        grouped_core_items = self.sort_core_repositories(core_items)
        self.verify_no_unknown_branch(grouped_core_items, CORE_BRANCHES)

        sorted_core_items = self.custom_sort(grouped_core_items, CORE_BRANCHES)

        category_order = CATEGORIES.keys()

        for branch, category_items in sorted_core_items.items():
            content += "\n\n\n## Code changes in the '" + branch + "' branch"

            sorted_category_items = self.custom_sort(category_items, category_order)

            for category, items in sorted_category_items.items():
                category_name = CATEGORIES[category] if category in CATEGORIES.keys() else category

                if category in CATEGORIES_REJECT_LIST:
                    continue

                content += "\n\n\n### " + category_name
                for item in items:
                    line = '* [#{pull_request_number}]({pull_request_url}): {pull_request_title}{thanks}'.format(
                        pull_request_number=item['number'],
                        pull_request_url=item['html_url'],
                        pull_request_title=item['title'],
                        thanks=self.thanks(item['user'])
                    )

                    content += "\n" + line

        del sorted_results['PrestaShop']

        content += "\n\n\n## Code changes in modules, themes & tools"

        for repository, items in sorted_results.items():
            content += "\n\n\n### " + repository
            for item in items:
                line = '* [#{pull_request_number}]({pull_request_url}): {pull_request_title}{thanks}'.format(
                    pull_request_number=item['number'],
                    pull_request_url=item['html_url'],
                    pull_request_title=item['title'],
                    thanks=self.thanks(item['user']),
                )

                content += "\n" + line

        return content

    def build_contributors_list(self, result):
        """Get contributor list

        :param result: GitHub Response
        :type result: dict
        :returns: Thanks message for all contributors
        :rtype: str

        """
        head = "\n\n\n<hr />\n\n"
        thanks = 'Thank you to the contributors whose pull requests were merged since the last Core Weekly Report: '

        return head + thanks + '' + self.get_authors(result['items']) + "!\n"

    def get_repositories(self, items, raw=False):
        """Get respositories and their items

        :param items: GitHub items response
        :type items: dict
        :param raw: Use raw name
        :type raw: bool
        :returns: Dict of repositories
        :rtype: dict

        """
        results = {}
        for item in items:
            repository = self.parser.extract_repository(item['html_url'], raw)
            if repository in results:
                results[repository].append(item)
            else:
                results.update({repository: []})
                results[repository].append(item)

        return results

    def get_authors(self, items):
        """Get author

        :param items: GitHub items response
        :type items: dict
        :returns: List of authors
        :rtype: str

        """
        authors = []
        for item in items:
            author = self.author_line(
                author_name=item['user']['login'],
                author_url=item['user']['html_url']
            )

            if author not in authors:
                authors.append(author)

        return ', '.join(authors)

    def sort_core_repositories(self, items):
        """Get PrestaShop repositories

        :param items: GitHub items response
        :type items: dict
        :returns: Sorted core repositories
        :rtype: dict

        """
        sorted_core_items = {}
        for item in items:
            category = self.parser.extract_core_category(item['body'])
            branch = self.parser.extract_branch(item['body'])

            if branch not in sorted_core_items:
                sorted_core_items.update({branch: {}})

            if category not in sorted_core_items[branch]:
                sorted_core_items[branch].update({category: []})

            sorted_core_items[branch][category].append(item)

        return sorted_core_items

    def build_stats_issues(self, opened, closed, fixed):
        """Build stats for issues

        :param opened: Stats about opened issues
        :type opened: dict
        :param closed: Stats about closed issues
        :type closed: dict
        :param fixed: Stats about fixed issues
        :type fixed: dict
        :returns: Stats for issues
        :rtype: str

        """
        return '''
Issues:

Opened: {total_opened_issues}
Closed: {total_closed_issues}
Fixed: {total_fixed_issues}
        '''.format(
            total_opened_issues=opened['total_count'],
            total_closed_issues=closed['total_count'],
            total_fixed_issues=fixed['total_count']
        )

    def build_stats_pull_requests(self, opened, closed, merged):
        """FIXME! briefly describe function

        :param opened: Stats about opened pull requests
        :type opened: dict
        :param closed: Stats about closed pull requests
        :type closed: dict
        :param merged: Stats about merged pull requests
        :type merged: dict
        :returns: Stats for pull requests
        :rtype: str

        """
        content = '''
Pull requests:

Opened: {total_opened_pull_requests}
PrestaShop:
{opened_branches}
Others:
{opened_repositories}

Closed: {total_closed_pull_requests}
PrestaShop:
{closed_branches}
Others:
{closed_repositories}

Merged: {total_fixed_pull_requests}
PrestaShop:
{merged_branches}
Others:
{merged_repositories}
        '''.format(
            total_opened_pull_requests=opened['total_count'],
            opened_branches=self.get_items_total_count(opened['core']['branches']),
            opened_repositories=self.get_items_total_count(opened['repositories']),
            total_closed_pull_requests=closed['total_count'],
            closed_branches=self.get_items_total_count(closed['core']['branches']),
            closed_repositories=self.get_items_total_count(closed['repositories']),
            total_fixed_pull_requests=merged['total_count'],
            merged_branches=self.get_items_total_count(merged['core']['branches']),
            merged_repositories=self.get_items_total_count(merged['repositories']),
        )

        return content

    def get_items_total_count(self, items):
        """Get items total count (key => value)

        :param items: Items
        :type items: dict
        :returns: String with key => value
        :rtype: str

        """
        return "\n".join(["\t{}: {}".format(item, str(total)) for item, total in items.items()])

    def get_issues_data(self, items):
        """Get stats data for a list of pull requests

        :param items: List of items
        :type items: dict
        :returns: Stats
        :rtype: dict

        """
        sorted_results = self.get_repositories(items, True)
        results = {
            'total_count': len(items),
            'repositories': {},
        }

        for repository, items in sorted_results.items():
            results['repositories'][repository] = {
                'total_count': len(items),
                'internal': 0,
                'external': 0,
            }
            for item in items:
                if item['user']['login'] in CORE_TEAM:
                    results['repositories'][repository]['internal'] += 1
                else:
                    results['repositories'][repository]['external'] += 1

        return results

    def get_pull_requests_data(self, items):
        """Get stats data for a list of issues

        :param items: List of items
        :type items: dict
        :returns: Stats
        :rtype: dict

        """
        sorted_results = self.get_repositories(items, True)
        core_items = sorted_results.get('PrestaShop')

        results = {
            'total_count': len(items),
            'core': {
                'branches': {},
                'internal': 0,
                'external': 0,
            },
            'repositories': {},
        }
        for item in core_items:
            branch = self.parser.extract_branch(item['body'])
            if branch:
                if branch not in CORE_BRANCHES:
                    branch = 'N/A'

                if branch in results['core']['branches']:
                    results['core']['branches'][branch] += 1
                else:
                    results['core']['branches'][branch] = 1

                if item['user']['login'] in CORE_TEAM:
                    results['core']['internal'] += 1
                else:
                    results['core']['external'] += 1

        # Now parse others repositories
        del sorted_results['PrestaShop']
        for repository, items in sorted_results.items():
            results['repositories'][repository] = {
                'total_count': len(items),
                'internal': 0,
                'external': 0,
            }
            for item in items:
                if item['user']['login'] in CORE_TEAM:
                    results['repositories'][repository]['internal'] += 1
                else:
                    results['repositories'][repository]['external'] += 1

        return results
