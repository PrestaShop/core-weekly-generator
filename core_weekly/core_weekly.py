# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .report import Report
from .template import Template
from .parser import Parser


class CoreWeekly():
    def __init__(self, args):
        self.report = Report(args.date_range, args.no_cache, args.debug)
        self.parser = Parser()
        self.template = Template(self.parser)
        self.date_range = args.date_range
        self.is_debug = args.debug

    ##
    # Generate Core weekly markdown content
    #
    def generate(self):
        opened_issues = self.report.get_opened_issues()
        closed_issues = self.report.get_closed_issues()
        fixed_issues = self.report.get_fixed_issues()
        merged_pull_requests = self.report.get_merged_pull_requests()

        if self.is_debug:
            opened_pull_requests = self.report.get_opened_pull_requests()
            closed_pull_requests = self.report.get_closed_pull_requests()

        content = self.template.headers()

        if self.is_debug:
            content += self.template.opened_issues(opened_issues)
            content += self.template.closed_issues(closed_issues)
            content += self.template.fixed_issues(fixed_issues)
            content += ''
            content += self.template.opened_pull_requests(opened_pull_requests)
            content += self.template.closed_pull_requests(closed_pull_requests)
            content += self.template.merged_pull_requests(merged_pull_requests)
            content += "\n\n\n"

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
        content += self.template.build_merged_pull_requests(merged_pull_requests)

        content += self.template.build_contributors_list(merged_pull_requests)
        content += self.template.footers()

        return content

    ##
    # Generate Core weekly community stats
    #
    def generate_community(self):
        # opened_issues = self.template.get_pull_requests_data(self.report.get_opened_issues())
        # closed_issues = self.template.get_pull_requests_data(self.report.get_closed_issues())
        # fixed_issues = self.template.get_pull_requests_data(self.report.get_fixed_issues())

        opened_pull_requests = self.template.get_pull_requests_data(self.report.get_opened_pull_requests()['items'])
        closed_pull_requests = self.template.get_pull_requests_data(self.report.get_closed_pull_requests()['items'])
        merged_pull_requests = self.template.get_pull_requests_data(self.report.get_merged_pull_requests()['items'])

        # content = self.template.build_community_issues(
        #     opened_issues,
        #     closed_issues,
        #     fixed_issues
        # )
        content = self.template.build_community_pull_requests(
            opened_pull_requests,
            closed_pull_requests,
            merged_pull_requests
        )

        return content
