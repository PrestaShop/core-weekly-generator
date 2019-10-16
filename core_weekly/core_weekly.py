# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .report import Report
from .template import Template
from .parser import Parser
import datetime
import re


class CoreWeekly():
    def __init__(self, args):
        """Constructor

        :param args: Arguments
        :type args: dict

        """
        self.date_range = self.get_date_range_from_week(args.date, args.year)
        self.report = Report(self.date_range, args.no_cache, args.debug)
        self.parser = Parser()
        self.template = Template(self.parser)
        self.is_debug = args.debug

    def get_date_range_from_week(self, date, year):
        """Get data range from week number

        :param date: Date or week number
        :type date: str
        :param year: Year
        :type year: str
        :returns: A date range
        :rtype: str
        """
        if not re.match(r'^\d+$', date):
            return date

        if year is None:
            year = datetime.datetime.now().year

        first_day = datetime.datetime.strptime(f'{year}-W{int(date )- 1}-1', "%Y-W%W-%w").date()
        last_day = first_day + datetime.timedelta(days=6.9)

        return str(first_day) + '..' + str(last_day)

    def generate(self):
        """Generate Core weekly markdown content

        :returns: Core weekly
        :rtype: str

        """
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
        content += self.template.pull_request_links(
            opened_issues,
            closed_issues,
            fixed_issues,
            self.date_range
        )
        content += self.template.build_merged_pull_requests(merged_pull_requests)

        content += self.template.build_contributors_list(merged_pull_requests)
        content += self.template.footers()

        return content

    def generate_stats(self):
        """Generate Core weekly community stats

        :returns: Generated stats content
        :rtype: str

        """
        # opened_issues = self.template.get_pull_requests_data(self.report.get_opened_issues())
        # closed_issues = self.template.get_pull_requests_data(self.report.get_closed_issues())
        # fixed_issues = self.template.get_pull_requests_data(self.report.get_fixed_issues())

        opened_pull_requests = self.template.get_pull_requests_data(self.report.get_opened_pull_requests()['items'])
        closed_pull_requests = self.template.get_pull_requests_data(self.report.get_closed_pull_requests()['items'])
        merged_pull_requests = self.template.get_pull_requests_data(self.report.get_merged_pull_requests()['items'])

        # content = self.template.build_stats_issues(
        #     opened_issues,
        #     closed_issues,
        #     fixed_issues
        # )
        content = self.template.build_stats_pull_requests(
            opened_pull_requests,
            closed_pull_requests,
            merged_pull_requests
        )

        return content
