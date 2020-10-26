import unittest

class BuildUrlTest(unittest.TestCase):
    # @unittest.expectedFailure
    def test_build_url(self):
        # build_url()がテスト対象の処理
        from booksearch.api import build_url
        expected = 'https://www.googleapis.com/books/v1/volumes?q=python'
        actual = build_url({'q':'python'})
        # アサーションメソッドの利用
        self.assertEqual(expected, actual, msg='このテストは失敗します')
