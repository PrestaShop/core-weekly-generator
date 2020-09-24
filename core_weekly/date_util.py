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


class DateUtil():
    def __init__(self):

        self.year = None
        self.month = None
        self.week = None
        self.first_day_number = None
        self.last_day_number = None

        self.date_range = None


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
