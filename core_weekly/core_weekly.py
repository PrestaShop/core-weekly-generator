# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .report import Report
from .template import Template
from .parser import Parser
from pathlib import Path
import datetime
import json
import logging
import re

logger = logging.getLogger(__name__)


class CoreWeekly():
    def __init__(self, args):
        """Constructor

        :param args: Arguments
        :type args: dict

        """
        self.year = None
        self.month = None
        self.week = None
        self.first_day_number = None
        self.last_day_number = None

        self.date_range = args.date
        if args.week is not None:
            self.date_range = self.get_date_range_from_week(args.week, args.year)

        if self.date_range:
            self.initialize_time_parameters(self.date_range)
            self.report = Report(self.date_range, args.no_cache, args.debug)
            self.parser = Parser()
            self.template = Template(self.parser)

        self.is_debug = args.debug
        self.directory = Path(__file__).resolve().parents[1] / 'var'

    def get_date_range_from_week(self, week, year):
        """Get data range from week number

        :param week: Week number
        :type week: str
        :param year: Year
        :type year: str
        :returns: A date range
        :rtype: str
        """
        if year is None:
            year = datetime.datetime.now().year

        self.year = year
        self.week = week

        first_day = datetime.datetime.strptime(f'{year}-W{int(week)-1}-1', "%Y-W%W-%w").date()
        last_day = first_day + datetime.timedelta(days=6.9)

        self.first_day_number = first_day.strftime('%-d')
        self.last_day_number = last_day.strftime('%-d')

        self.month = datetime.datetime.strptime(f'{year}-W{int(week)-1}-1', "%Y-W%W-%w").date().strftime('%B')

        return str(first_day) + '..' + str(last_day)


    def initialize_time_parameters(self, date_range):

        split = date_range.split('..')
        first_date = datetime.datetime.strptime(split[0], "%Y-%m-%d").date()
        last_date = datetime.datetime.strptime(split[1], "%Y-%m-%d").date()

        if self.first_day_number is None:
            self.first_day_number = first_date.strftime('%-d')
        if self.last_day_number is None:
            self.last_day_number = last_date.strftime('%-d')

        if self.year is None:
            self.year = first_date.strftime('%Y')
        
        if self.month is None:
            self.month = last_date.strftime('%B')

        if self.week is None:
            self.week = (last_date++ datetime.timedelta(days=6.9)).strftime('%W')


    def generate(self):
        """Generate Core weekly markdown content

        :returns: Core weekly
        :rtype: str

        """
        opened_issues = self.report.get_opened_issues()
        closed_issues = self.report.get_closed_issues()
        fixed_issues = self.report.get_fixed_issues()
        merged_pull_requests = self.report.get_merged_pull_requests()
        opened_pull_requests = self.report.get_opened_pull_requests()
        closed_pull_requests = self.report.get_closed_pull_requests()

        content = self.template.headers(self.first_day_number, self.last_day_number, self.week, self.month,self.year)

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
            opened_pull_requests,
            closed_pull_requests,
            merged_pull_requests,
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
        opened_issues = self.template.get_issues_data(self.report.get_opened_issues()['items'])
        closed_issues = self.template.get_issues_data(self.report.get_closed_issues()['items'])
        fixed_issues = self.template.get_issues_data(self.report.get_fixed_issues()['items'])

        opened_pull_requests = self.template.get_pull_requests_data(self.report.get_opened_pull_requests()['items'])
        closed_pull_requests = self.template.get_pull_requests_data(self.report.get_closed_pull_requests()['items'])
        merged_pull_requests = self.template.get_pull_requests_data(self.report.get_merged_pull_requests()['items'])

        content = self.template.build_stats_issues(
            opened_issues,
            closed_issues,
            fixed_issues
        )
        content += self.template.build_stats_pull_requests(
            opened_pull_requests,
            closed_pull_requests,
            merged_pull_requests
        )

        if self.year and self.week:
            directory = self.directory / str(self.year)
            logger.debug('Create directory: {}'.format(directory))
            Path.mkdir(directory, parents=False, exist_ok=True)
            self.save_json(
                directory,
                'issues',
                {
                    'opened': opened_issues,
                    'closed': closed_issues,
                    'fixed': fixed_issues,
                }
            )
            self.save_json(
                directory,
                'pull_requests',
                {
                    'opened': opened_pull_requests,
                    'closed': closed_pull_requests,
                    'merged': merged_pull_requests,
                }
            )

        return content

    def save_json(self, directory, filename, data):
        """Save data into json file

        :param directory: Directory name
        :type directory: str
        :param filename: File name
        :type filename: str
        :param data: Data to save
        :type data: dict

        """
        with open(directory / str(str(self.week) + '_' + filename + '.json'), 'w') as jsonfile:
            json.dump(data, jsonfile)

    def compute_files(self):
        p = Path(self.directory)
        data = {}
        for directory in p.iterdir():
            if not directory.is_dir():
                continue

            year = directory.name
            data[year] = {
                'pull_requests': {},
                'issues': {},
            }

            for f in list(p.glob(year + '/*.json')):
                matches = re.search(r'^(\d+)_(\w+)\.json$', f.name)
                if not matches:
                    continue

                week = int(matches.group(1))
                typ = matches.group(2)
                if week not in data[year][typ]:
                    data[year][typ].update({week: []})

                data[year][typ][week] = json.loads(Path(f).read_text())

        with open(self.directory / '../public/computed.json', 'w') as jsonfile:
            json.dump(data, jsonfile)
