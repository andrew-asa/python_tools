import unittest
from python_tools.utils.DateUtils import *


class TestMathFunc(unittest.TestCase):

    def test_YY_MM_DD(self):
        print(getYY_MM_DD())
    def test_get_date_str(self):
        print(get_date_str("%Y-%m-%d-%H:%M:%S"))
if __name__ == '__main__':
    unittest.main()
