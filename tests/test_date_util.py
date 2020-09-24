import unittest
from core_weekly.date_util import DateUtil

class TestDateUtil(unittest.TestCase):

    def test_get_date_range_from_week_23_2020(self):
        date_util = DateUtil()
        self.assertEqual(date_util.get_date_range_from_week(23, 2020), '2020-06-01..2020-06-07')

    def test_get_date_range_from_week_38_2020(self):
        date_util = DateUtil()
        self.assertEqual(date_util.get_date_range_from_week(38, 2020), '2020-09-14..2020-09-20')

if __name__ == '__main__':
    unittest.main()