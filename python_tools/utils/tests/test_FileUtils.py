import unittest
import os
from python_tools.utils.FileNameUtils import FileNameUtils
from python_tools.utils.FileUtils import FileUtils


class TestFileUtils(unittest.TestCase):

    def test_join(self):
        bp = '/Users/andrew_asa/Documents/code/github/andrew-asa/exec/python/out'
        FileUtils.emptyDir(bp)


if __name__ == '__main__':
    unittest.main()
