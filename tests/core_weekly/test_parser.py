import unittest
from core_weekly.parser import Parser


class TestParser(unittest.TestCase):
    def test_extract_repository(self):
        parser = Parser()
        self.assertEqual(parser.extract_repository('https://github.com/PrestaShop/nightly-board/pull/47'), 'Nightly board')

    def test_extract_branch(self):
        parser = Parser()
        payload = '''

| Questions     | Answers
| ------------- | -------------------------------------------------------
| Branch?       | 1.7.7.x
| Description?  | Abcd
| Type?         | bug fix
| Category?     | BO
| BC breaks?    | no
| Deprecations? | no
| Fixed ticket? | Fixes #10000
| How to test?  | Please check #10000

        '''
        self.assertEqual(parser.extract_branch(payload), '1.7.7.x')

    def test_extract_core_category(self):
        parser = Parser()
        payload = '''

| Questions     | Answers
| ------------- | -------------------------------------------------------
| Branch?       | 1.7.7.x
| Description?  | Abcd
| Type?         | bug fix
| Category?     | BO
| BC breaks?    | no
| Deprecations? | no
| Fixed ticket? | Fixes #10000
| How to test?  | Please check #10000

        '''
        self.assertEqual(parser.extract_core_category(payload), 'BO')
