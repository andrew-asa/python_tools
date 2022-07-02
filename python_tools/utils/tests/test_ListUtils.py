import unittest
from python_tools.utils.ListUtils import *


class TestListUtils(unittest.TestCase):

    def test_coordinateCompare(self):
        self.assertTrue(ListUtils.isEmptyList([]))
        self.assertFalse(ListUtils.isEmptyList([1]))
    def test_joinTwoDimensionList(self):
        print(ListUtils.joinTwoDimensionList([['上','下'],['左','右']]))
if __name__ == '__main__':
    unittest.main()
