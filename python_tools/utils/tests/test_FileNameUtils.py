import unittest
import os
from python_tools.utils.FileNameUtils import FileNameUtils


class TestFileNameUtils(unittest.TestCase):

    def test_join(self):
        self.assertEqual("/dst/a.png",FileNameUtils.join("/dst","a.png"))
        self.assertEqual("/dst/bc/a.png",FileNameUtils.join("/dst","bc","a.png"))

if __name__ == '__main__':
    unittest.main()
