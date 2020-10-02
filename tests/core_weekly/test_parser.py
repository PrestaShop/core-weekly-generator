import unittest
from core_weekly.parser import Parser


class TestParser(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()

    def test_extract_repository(self):
        self.assertEqual(self.parser.extract_repository('https://github.com/PrestaShop/nightly-board/pull/47'), 'Nightly board')

    def test_extract_repository_without_match(self):
        self.assertEqual(
            self.parser.extract_repository('https://github.com/PierreRambaud/nightly-board/pull/47'),
            'https://github.com/PierreRambaud/nightly-board/pull/47'
        )

    def test_extract_repository_without_in_project_list(self):
        self.assertEqual(
            self.parser.extract_repository('https://github.com/PrestaShop/superawesomeprojectthatarenotinthelist/pull/42'),
            'superawesomeprojectthatarenotinthelist'
        )

    def test_extract_branch_without_body(self):
        self.assertIsNone(self.parser.extract_branch(None))

    def test_extract_branch(self):
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
        self.assertEqual(self.parser.extract_branch(payload), '1.7.7.x')

    def test_extract_branch_without_valid_name(self):
        payload = '''
| Questions     | Answers
| ------------- | -------------------------------------------------------
| Branch?       |
| Description?  | Abcd
| Type?         | bug fix
| Category?     | BO
| BC breaks?    | no
| Deprecations? | no
| Fixed ticket? | Fixes #10000
| How to test?  | Please check #10000
'''
        self.assertEqual(self.parser.extract_branch(payload), 'unknown branch')

    def test_extract_core_category(self):
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
        self.assertEqual(self.parser.extract_core_category(payload), 'BO')

    def test_extract_core_category_without_body(self):
        self.assertIsNone(self.parser.extract_core_category(None))

    def test_extract_core_category_without_valid_category(self):
        payload = '''
| Questions     | Answers
| ------------- | -------------------------------------------------------
| Branch?       | 1.7.7.x
| Description?  | Abcd
| Type?         | bug fix
| Category?     |
| BC breaks?    | no
| Deprecations? | no
| Fixed ticket? | Fixes #10000
| How to test?  | Please check #10000
'''

        self.assertEqual(self.parser.extract_core_category(payload), 'Misc')
