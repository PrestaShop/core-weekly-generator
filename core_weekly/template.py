# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from coreteam import CORE_BRANCHES
from coreteam import CORE_TEAM
from coreteam import CATEGORIES
from collections import OrderedDict


class Template():
    def __init__(self, parser):
        self.parser = parser

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
    def opened_pull_requests(self, result):
        return 'Opened pull requests: {opened_pull_requests_count}, Incomplete results: {query_incomplete_results}'.format(
            opened_pull_requests_count=result['total_count'],
            query_incomplete_results=result['incomplete_results']
        )

    ##
    # Get closed pull requests count and status
    #
    def closed_pull_requests(self, result):
        return 'Closed pull requests: {closed_pull_requests_count}, Incomplete results: {query_incomplete_results}'.format(
            closed_pull_requests_count=result['total_count'],
            query_incomplete_results=result['incomplete_results']
        )

    ##
    # Get merged pull requests count and status
    #
    def merged_pull_requests(self, result):
        return 'Merged pull requests: {merged_pull_requests_count}, Incomplete results: {query_incomplete_results}'.format(
            merged_pull_requests_count=result['total_count'],
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
    def pr_links(self, opened_pull_requests, closed_pull_requests, merged_pull_requests, date_range):
        return '''- [{opened_pull_requests_count} pull requests have been opened](https://github.com/search?q=org%3APrestaShop+is%3Apublic++-repo%3Aprestashop%2Fprestashop.github.io++is%3Apr+created%3A{date_range}) in the project repositories;
- [{closed_pull_requests_count} pull requests have been closed](https://github.com/search?q=org%3APrestaShop+is%3Apublic++-repo%3Aprestashop%2Fprestashop.github.io++is%3Apr+closed%3A{date_range}), including [{merged_pull_requests_count} merged pull requests](https://github.com/search?q=org%3APrestaShop+is%3Apublic++-repo%3Aprestashop%2Fprestashop.github.io++is%3Apr+merged%3A{date_range}).
        '''.format(
            opened_pull_requests_count=opened_pull_requests['total_count'],
            closed_pull_requests_count=closed_pull_requests['total_count'],
            merged_pull_requests_count=merged_pull_requests['total_count'],
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
            message = ', by '
        else:
            message = '. Thank you '

        return message + self.author_line(
            author_name=user['login'],
            author_url=user['html_url'],
        )

    ##
    # Generate author markdown links
    #
    # :param str author_name: Author name
    # :param str author_url: Author ulr
    #
    # :return str
    #
    def author_line(self, author_name, author_url, **kwargs):
        return '[@{author_name}]({author_url})'.format(
            author_name=author_name,
            author_url=author_url,
        )

    ##
    # Sort core items by branch following given branch order
    #
    # thanks https://stackoverflow.com/questions/12031482/custom-sorting-python-dictionary
    #
    def custom_sort(self, dict1, key_order):
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

        sorted_core_items = self.custom_sort(grouped_core_items, CORE_BRANCHES)

        category_order = CATEGORIES.keys()

        for branch, category_items in sorted_core_items.items():
            content += "\n\n## Code changes in the '" + branch + "' branch (for vXXXX)"

            sorted_category_items = self.custom_sort(category_items, category_order)

            for category, items in sorted_category_items.items():
                category_name = CATEGORIES[category] if category in CATEGORIES.keys() else category

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

        content += "\n\n## Code changes in modules, themes & tools"

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

    ##
    # Get contributor list
    #
    # :param dict result List of pull requests
    #
    # :param str
    #
    def build_contributors_list(self, result):
        head = "\n\n<hr />\n\n"
        thanks = 'Thank you to the contributors whose pull requests were merged since the last Core Weekly Report: '

        return head + thanks + '' + self.get_authors(result['items']) + "!\n"

    ##
    # Get Repositories
    #
    # :param dict items: Repositories
    #
    # :return dict
    #
    def get_repositories(self, items):
        results = {}
        for item in items:
            repository = self.parser.extract_repository(item['html_url'])
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
    # :return str
    #
    def get_authors(self, items):
        authors = []
        for item in items:
            authors.append(
                self.author_line(
                    author_name=item['user']['login'],
                    author_url=item['user']['html_url']
                )
            )

        return ', '.join(authors)

    ##
    # Get PrestaShop repositories
    #
    # :param dict items: Repositories
    #
    def sort_core_repositories(self, items):
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

    ##
    # Build community issues
    #
    # :param dict opened: Stats about opened issues
    # :param dict closed: Stats about closed issues
    # :param dict fixed: Stats about fixed issues
    #
    # return str
    #
    def build_community_issues(self, opened, closed, fixed):
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

    ##
    # Build community issues
    #
    # :param dict opened: Stats about opened pull requests
    # :param dict closed: Stats about closed pull requests
    # :param dict merged: Stats about merged pull requests
    #
    # return str
    #
    def build_community_pull_requests(self, opened, closed, merged):
        content = '''
Pull requests:

Opened: {total_opened_pull_requests}
PrestaShop:
{opened_branches}
{opened_repositories}

Closed: {total_closed_pull_requests}
PrestaShop:
{closed_branches}
{closed_repositories}

Merged: {total_fixed_pull_requests}
PrestaShop:
{merged_branches}
{merged_repositories}
        '''.format(
            total_opened_pull_requests=opened['total_count'],
            opened_branches=self.get_items_total_count(opened['branches']),
            opened_repositories=self.get_items_total_count(opened['repositories']),
            total_closed_pull_requests=closed['total_count'],
            closed_branches=self.get_items_total_count(closed['branches']),
            closed_repositories=self.get_items_total_count(closed['repositories']),
            total_fixed_pull_requests=merged['total_count'],
            merged_branches=self.get_items_total_count(merged['branches']),
            merged_repositories=self.get_items_total_count(merged['repositories']),
        )

        return content

    def get_items_total_count(self, items):
        return "\n".join(["\t{}: {}".format(item, str(total)) for item, total in items.items()])

    ##
    # Get community data for a list of items
    #
    # :param list items: List of items
    #
    def get_pull_requests_data(self, items):
        sorted_results = self.get_repositories(items)
        core_items = sorted_results.get('PrestaShop')

        results = {
            'total_count': len(items),
            'branches': {},
            'repositories': {},
        }
        for item in core_items:
            branch = self.parser.extract_branch(item['body'])
            if branch:
                if branch in results['branches']:
                    results['branches'][branch] += 1
                else:
                    results['branches'][branch] = 1

        # Now parse others repositories
        del sorted_results['PrestaShop']
        for repository, items in sorted_results.items():
            results['repositories'][repository] = len(items)

        return results
