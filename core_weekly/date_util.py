# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from datetime import date
import logging

logger = logging.getLogger(__name__)


class DateUtil():
    def __init__(self):

        self.year = None
        self.month = None
        self.week = None
        self.first_day_number = None
        self.last_day_number = None

        self.date_range = None

    def get_date_range_from_week(self, week, year=None):
        """Get data range from week number

        :param week: Week number
        :type week: str
        :param year: Year
        :type year: str, optional
        :returns: A date range
        :rtype: str
        """
        if year is None:
            year = datetime.datetime.now().year

        self.year = year
        self.week = week

        first_day = datetime.datetime.strptime(f'{year}-W{int(week)}-1', "%G-W%V-%u").date()
        last_day = first_day + datetime.timedelta(days=6.9)

        self.first_day_number = first_day.strftime('%-d')
        self.last_day_number = last_day.strftime('%-d')

        self.month = first_day.strftime('%B')

        return str(first_day) + '..' + str(last_day)

    def format_day_number(self, day_number):
        day_numbers = {
            1: '1st',
            2: '2nd',
            3: '3rd',
        }

        return day_numbers.get(day_number, str(day_number) + 'th')

    def compute_from_day_to_day_statement(self, date_range):

        split = date_range.split('..')
        first_date = datetime.datetime.strptime(split[0], "%Y-%m-%d").date()
        last_date = datetime.datetime.strptime(split[1], "%Y-%m-%d").date()

        first_day_number = int(first_date.strftime('%-d'))
        last_day_number = int(last_date.strftime('%-d'))
        first_month_number = first_date.strftime('%B')
        last_month_number = last_date.strftime('%B')
        first_year_number = first_date.strftime('%Y')
        last_year_number = last_date.strftime('%Y')

        last_day_part = '{} of {} {}'.format(
            self.format_day_number(last_day_number),
            last_month_number,
            last_year_number
        )

        first_day_part = self.format_day_number(first_day_number)
        if first_month_number != last_month_number:
            first_day_part = '{} of {}'.format(
                first_day_part,
                first_month_number
            )
        if first_year_number != last_year_number:
            first_day_part = first_day_part + ' ' + first_year_number

        return 'from Monday {} to Sunday {}'.format(
            first_day_part,
            last_day_part
        )
