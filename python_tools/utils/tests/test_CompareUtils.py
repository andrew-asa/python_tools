import unittest
from python_tools.utils.CompareUtils import *


class TestCompareUtils(unittest.TestCase):

    def test_coordinateCompare(self):
        obj1 = [0, 0]
        obj2 = [0, 1]
        self.assertEqual(-1, CompareUtils.coordinateCompare([0, 0], [0, 1]))
        self.assertEqual(0, CompareUtils.coordinateCompare([0, 0], [0, 0]))
        self.assertEqual(-1, CompareUtils.coordinateCompare([2, 3], [2, 4]))
        self.assertEqual(-1, CompareUtils.coordinateCompare([3, 3], [2, 4]))
        self.assertEqual(1, CompareUtils.coordinateCompare([3, 4], [2, 4]))

    def test_coordinateSort(self):
        points = [[1, 1], [0, 0]];
        CompareUtils.coordinateSort(points)
        self.assertEqual([[0, 0], [1, 1]], points)
        points = [[1, 1], [2, 2]];
        CompareUtils.coordinateSort(points)
        self.assertEqual([[1, 1], [2, 2]], points)
        points = [[3, 3], [2, 2], [1, 1]];
        CompareUtils.coordinateSort(points)
        self.assertEqual([[1, 1], [2, 2], [3, 3]], points)
        points = [[0, 3], [0, 2], [1, 3],[2,1]];
        CompareUtils.coordinateSort(points)
        self.assertEqual([[2, 1], [0, 2], [0, 3],[1,3]], points)

if __name__ == '__main__':
    unittest.main()
