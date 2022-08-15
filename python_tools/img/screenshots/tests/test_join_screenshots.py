import unittest

from python_tools.img.screenshots.join_screenshots import Screenshot_Join
from python_tools.ocr.img_ocr import ImageOcr
from python_tools.utils.ClipboardUtils import ClipboardUtils
from python_tools.utils.StringUtils import StringUtils


class TesScreenshot_Join(unittest.TestCase):
    join = Screenshot_Join()

    def test_join(self):
        path = "/Users/andrew_asa/Documents/code/github/andrew-asa/exec/python/python_tools/res/join_screenshots/"
        img = "1.png;2.png"
        self.join.join(path,img)
    def test_getAllFile(self):
        path="/Users/andrew_asa/Documents/code/github/andrew-asa/exec/python/python_tools/res/join_screenshots/"
        img="1.png;2.png"
        print(self.join.getAllImg(path,img))




if __name__ == '__main__':
    unittest.main()
