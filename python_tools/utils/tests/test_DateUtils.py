import unittest
from python_tools.utils.DateUtils import DateUtils


class TestDateUtils(unittest.TestCase):

    def test_YY_MM_DD(self):
        print(DateUtils.getYY_MM_DD())
    def test_get_date_str(self):
        print(DateUtils.get_date_str("%Y-%m-%d-%H:%M:%S"))
        print(DateUtils.get_date_str(DateUtils.yy_mm_dd))
if __name__ == '__main__':
    unittest.main()
