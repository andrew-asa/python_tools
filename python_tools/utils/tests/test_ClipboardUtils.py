import unittest

from python_tools.utils.DateUtils import DateUtils
from python_tools.utils.ClipboardUtils import ClipboardUtils


class TesClipboardUtils(unittest.TestCase):

    def test_coordinateCompare(self):
        ClipboardUtils.copyToClipboard("测试")
        self.assertEqual(ClipboardUtils.copyFromClipboard(),"测试")
    @unittest.skip('skipped test_copyImageTo')
    def test_copyImageTo(self):
        fn = DateUtils.get_date_str("%Y-%m-%d-%H-%M-%S") + ".png"
        print(fn)
        ClipboardUtils.copyImageTo(fn)


if __name__ == '__main__':
    unittest.main()
