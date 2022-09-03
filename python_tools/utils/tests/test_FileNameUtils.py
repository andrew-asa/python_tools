import unittest
import os
from python_tools.utils.FileNameUtils import FileNameUtils


class TestFileNameUtils(unittest.TestCase):

    def test_join(self):
        self.assertEqual("a.png",FileNameUtils.join("","a.png"))
        self.assertEqual("/dst/a.png",FileNameUtils.join("/dst","a.png"))
        self.assertEqual("/dst/bc/a.png",FileNameUtils.join("/dst","bc","a.png"))
    def test_dirname(self):
        self.assertEqual('/abc',FileNameUtils.dirname("/abc/t.txt"))
        self.assertEqual('/abc/bcd',FileNameUtils.dirname("/abc/bcd/t.txt"))
        self.assertEqual('/abc/bcd',FileNameUtils.dirname("/abc/bcd/efg"))
        self.assertEqual('/abc/bcd',FileNameUtils.dirname("/abc/bcd/efg/"))
    def test_base_name(self):
        self.assertEqual('t.txt',FileNameUtils.base_name("/abc/t.txt"))
        self.assertEqual('abc',FileNameUtils.base_name("/abc"))
if __name__ == '__main__':
    unittest.main()
