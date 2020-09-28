import unittest
from core_weekly.date_util import DateUtil


class TestDateUtil(unittest.TestCase):
    def test_get_date_range_from_week_23_2020(self):
        date_util = DateUtil()
        self.assertEqual(date_util.get_date_range_from_week(23, 2020), '2020-06-01..2020-06-07')

    def test_get_date_range_from_week_38_2020(self):
        date_util = DateUtil()
        self.assertEqual(date_util.get_date_range_from_week(38, 2020), '2020-09-14..2020-09-20')

    def test_format_day_number_2nd(self):
        date_util = DateUtil()
        self.assertEqual(date_util.format_day_number(2), '2nd')

    def test_format_day_number_28nd(self):
        date_util = DateUtil()
        self.assertEqual(date_util.format_day_number(28), '28th')

    def test_compute_from_day_to_day_statement_week_23_2020(self):
        date_util = DateUtil()
        self.assertEqual(
            date_util.compute_from_day_to_day_statement('2020-06-01..2020-06-07'),
            'from Monday 1st to Sunday 7th of June 2020'
        )

    def test_compute_from_day_to_day_statement_week_38_2020(self):
        date_util = DateUtil()
        self.assertEqual(
            date_util.compute_from_day_to_day_statement('2020-09-14..2020-09-20'),
            'from Monday 14th to Sunday 20th of September 2020'
        )

    def test_compute_from_day_to_day_statement_week_01_2020(self):
        date_util = DateUtil()
        self.assertEqual(
            date_util.compute_from_day_to_day_statement('2019-12-30..2020-01-05'),
            'from Monday 30th of December 2019 to Sunday 5th of January 2020'
        )
