import unittest

from python_tools.ocr.img_ocr import ImageOcr


class TestMathFunc(unittest.TestCase):
    ocr = ImageOcr()

    def test_ocrPointCompare(self):
        obj1 = [[[121.0, 35.0], [305.0, 35.0], [305.0, 82.0], [121.0, 82.0]], ('阴经(脏)', 0.8616531491279602)]
        obj2 = [[[458.0, 35.0], [637.0, 35.0], [637.0, 82.0], [458.0, 82.0]], ('阳经()', 0.8003172874450684)]
        self.assertEqual(-1, self.ocr.ocrPointCompare(obj1, obj2))

    def test_get_result_line_content(self):
        line = [[[121.0, 35.0], [305.0, 35.0], [305.0, 82.0], [121.0, 82.0]], ('阴经(脏)', 0.8616531491279602)];
        self.assertEqual(self.ocr.getResultLineContent(line), '阴经(脏)')

    def test_joinResultString(self):
        result = [
            [[[121.0, 35.0], [305.0, 35.0], [305.0, 82.0], [121.0, 82.0]], ('上', 0.8616531491279602)],
            [[[458.0, 35.0], [637.0, 35.0], [637.0, 82.0], [458.0, 82.0]], ('下', 0.8003172874450684)],
        ]
        self.assertEqual("上,下", self.ocr.joinResultString(result, ","))
        self.assertEqual("上下", self.ocr.joinResultString(result))

    def test_ocr_result_sort(self):
        result = [
            [[[121.0, 35.0], [305.0, 35.0], [305.0, 82.0], [121.0, 82.0]], ('上', 0.8616531491279602)],
            [[[458.0, 35.0], [637.0, 35.0], [637.0, 82.0], [458.0, 82.0]], ('下', 0.8003172874450684)],
        ]
        self.ocr.sortOcrResult(result)
        self.assertEqual("上下", self.ocr.joinResultString(result))

        result = [
            [[[121.0, 35.0], [305.0, 35.0], [305.0, 82.0], [121.0, 82.0]], ('下', 0.8616531491279602)],
            [[[458.0, 25.0], [637.0, 35.0], [637.0, 82.0], [458.0, 82.0]], ('上', 0.8003172874450684)],
        ]
        self.ocr.sortOcrResult(result)
        self.assertEqual("上下", self.ocr.joinResultString(result))

    def test_ocr_result_sort(self):
        result = [
            [[[440.0, 35.0], [305.0, 35.0], [305.0, 82.0], [121.0, 82.0]], ('下', 0.8616531491279602)],
            [[[450.0, 35.0], [637.0, 35.0], [637.0, 82.0], [458.0, 82.0]], ('左', 0.8003172874450684)],
            [[[458.0, 35.0], [637.0, 35.0], [637.0, 82.0], [458.0, 82.0]], ('右', 0.8003172874450684)],
            [[[458.0, 25.0], [637.0, 35.0], [637.0, 82.0], [458.0, 82.0]], ('上', 0.8003172874450684)],
        ]
        self.ocr.sortOcrResult(result)
        self.assertEqual("上下左右", self.ocr.joinResultString(result))
    def testScanOrderResult(self):
        result = [
            [[[440.0, 35.0], [305.0, 35.0], [305.0, 82.0], [121.0, 82.0]], ('上', 0.8616531491279602)],
            [[[450.0, 35.0], [637.0, 35.0], [637.0, 82.0], [458.0, 82.0]], ('下', 0.8003172874450684)],
            [[[400.0, 45.0], [637.0, 35.0], [637.0, 82.0], [458.0, 82.0]], ('左', 0.8003172874450684)],
            [[[458.0, 45.0], [637.0, 35.0], [637.0, 82.0], [458.0, 82.0]], ('右', 0.8003172874450684)],
        ]
        ret = self.ocr.scanOrderResult(result)
        self.assertEqual([['上', '下'], ['左', '右']],ret)
    # @unittest.skip
    def test_ocr_clipboard_img(self):
        self.ocr.ocr_clipboard_img()


if __name__ == '__main__':
    unittest.main()
