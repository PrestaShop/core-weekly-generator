# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .github import GitHub
from .template import Template


class CoreWeekly():
    def __init__(self, args):
        self.github = GitHub(args.no_cache)
        self.template = Template()
        self.date_range = args.date_range

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
        # opened_pr = self.get_opened_pr()
        # closed_pr = self.get_closed_pr()
        merged_pr = self.get_merged_pr()

        content = self.template.headers()

        # debug only
        # content += self.template.opened_issues(opened_issues)
        # content += self.template.closed_issues(closed_issues)
        # content += self.template.fixed_issues(fixed_issues)
        # content += ''
        # content += self.template.opened_pr(opened_pr)
        # content += self.template.closed_pr(closed_pr)
        # content += self.template.merged_pr(merged_pr)
        # content += ''
        # content += "\n\n"

        content += self.template.issues_links(
            opened_issues,
            closed_issues,
            fixed_issues,
            self.date_range
        )
        content += self.template.pr_links(
            opened_issues,
            closed_issues,
            fixed_issues,
            self.date_range
        )
        content += self.template.build_merged_pull_requests(merged_pr)

        content += self.template.build_contributors_list(merged_pr)
        content += self.template.footers()

        return content
