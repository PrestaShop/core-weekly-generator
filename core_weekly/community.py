# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .github import GitHub


class Community():
    def __init__(self, args):
        self.github = GitHub(args.no_cache, args.debug)
        self.date_range = args.date_range
        self.is_debug = args.debug

    ##
    # Get opened issues
    #
    def get_pull_requests(self):
        return self.github.get_json(
            'updated:{date_range}'.format(date_range=self.date_range),
            False
        )

    ##
    # Get closed issues
    #
    def get_issues(self):
        return self.github.get_json(
            'updated:{date_range}'.format(date_range=self.date_range)
        )

    ##
    # Generate Core weekly markdown content
    #
    def generate(self):
        issues = self.parse_issues(self.get_issues()['items'])
        pull_requests = self.parse_pull_requests(self.get_pull_requests()['items'])



        # pull_requestsint(issues)
        return ''

    def parse_issues(self, issues):
        results = {}
        for issue in issues:
            state = issue['state']
            if state in results:
                results[state].append(issue)
            else:
                results.update({state: []})
                results[state].append(issue)

        return results

    def parse_pull_requests(self, pull_requests):
        results = {}
        for pull_request in pull_requests:
            state = pull_request['state']
            if state == 'closed':
                print(pull_request)
                exit(1)
            if state in results:
                results[state].append(pull_request)
            else:
                results.update({state: []})
                results[state].append(pull_request)

        print(results.keys())
        return results
