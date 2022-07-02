import unittest
from python_tools.utils.StringUtils import *


class TestStringUtils(unittest.TestCase):

    def test_isEmpty(self):
        self.assertTrue(StringUtils.isEmpty(""))
        self.assertTrue(StringUtils.isEmpty())
        self.assertFalse(StringUtils.isEmpty("a"))
    def test_isNoEmpty(self):
        self.assertTrue(StringUtils.isNoEmpty("aaa"))
        self.assertFalse(StringUtils.isNoEmpty(""))
        self.assertFalse(StringUtils.isNoEmpty())

if __name__ == '__main__':
    unittest.main()
