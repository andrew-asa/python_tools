import unittest
from python_tools.utils.ClipboardUtils import *


class TesClipboardUtils(unittest.TestCase):

    def test_coordinateCompare(self):
        ClipboardUtils.copyToClipboard("测试")
        self.assertEqual(ClipboardUtils.copyFromClipboard(),"测试")



if __name__ == '__main__':
    unittest.main()
