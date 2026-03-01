from unittest import TestCase


def add(a, b):
    return a + b


def return_none():
    return None


class TestUnitTestClass(TestCase):
    """test_unittest のテストクラス"""

    def test_method(self):
        """addのテスト"""
        result = add(1, 2)
        self.assertEqual(result, 3)
