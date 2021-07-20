import unittest
from core_weekly.date_util import DateUtil


class TestDateUtil(unittest.TestCase):
    def setUp(self):
        self.date_util = DateUtil()

    def test_get_date_range_from_week_1_2020(self):
        self.assertEqual(self.date_util.get_date_range_from_week(1, 2020), '2019-12-30..2020-01-05')

    def test_get_date_range_from_week_23_2020(self):
        self.assertEqual(self.date_util.get_date_range_from_week(23, 2020), '2020-06-01..2020-06-07')

    def test_get_date_range_from_week_38_2020(self):
        self.assertEqual(self.date_util.get_date_range_from_week(38, 2020), '2020-09-14..2020-09-20')

    def test_get_date_range_from_week_1_2021(self):
        self.assertEqual(self.date_util.get_date_range_from_week(1, 2021), '2021-01-04..2021-01-10')

    def test_get_date_range_from_week_28_2021(self):
        self.assertEqual(self.date_util.get_date_range_from_week(28, 2021), '2021-07-12..2021-07-18')

    def test_format_day_number_2nd(self):
        self.assertEqual(self.date_util.format_day_number(2), '2nd')

    def test_format_day_number_28nd(self):
        self.assertEqual(self.date_util.format_day_number(28), '28th')

    def test_compute_from_day_to_day_statement_week_23_2020(self):
        self.assertEqual(
            self.date_util.compute_from_day_to_day_statement('2020-06-01..2020-06-07'),
            'from Monday 1st to Sunday 7th of June 2020'
        )

    def test_compute_from_day_to_day_statement_week_38_2020(self):
        self.assertEqual(
            self.date_util.compute_from_day_to_day_statement('2020-09-14..2020-09-20'),
            'from Monday 14th to Sunday 20th of September 2020'
        )

    def test_compute_from_day_to_day_statement_week_01_2020(self):
        self.assertEqual(
            self.date_util.compute_from_day_to_day_statement('2019-12-30..2020-01-05'),
            'from Monday 30th of December 2019 to Sunday 5th of January 2020'
        )
