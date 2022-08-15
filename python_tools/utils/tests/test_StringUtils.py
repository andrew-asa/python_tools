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
    def test_endswith(self):
        self.assertTrue(StringUtils.endswith("abc/e",'e'))
        self.assertTrue(StringUtils.endswith("abc/",'/'))
        self.assertFalse(StringUtils.endswith("abc/c",'/'))
        self.assertFalse(StringUtils.endswith('',''))

if __name__ == '__main__':
    unittest.main()
