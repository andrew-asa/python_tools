import unittest

from python_tools.img.img_draw import Imgage_Draw
from python_tools.img.screenshots.join_screenshots import Screenshot_Join
from python_tools.ocr.img_ocr import ImageOcr
from python_tools.utils.ClipboardUtils import ClipboardUtils
from python_tools.utils.FileNameUtils import FileNameUtils
from python_tools.utils.StringUtils import StringUtils
import cv2


class TesScreenshot_Join(unittest.TestCase):
    join = Screenshot_Join()
    path = "/Users/andrew_asa/Documents/code/github/andrew-asa/exec/python/python_tools/res/join_screenshots/"

    def test_join(self):
        img = "1.png;2.png"
        self.join.join(self.path, img)

    def test_getAllFile(self):
        img = "1.png;2.png"
        print(self.join.getAllImg(self.path, img))

    def test_ocr(self):
        ocr = ImageOcr()
        img = FileNameUtils.join(self.path, "2.png")
        ocrResult = ocr.ocr(img, False)
        print(ocrResult)
        ocr.sortOcrResult(ocrResult)
        print(ocrResult)

    def test_getRectangle(self):
        ocr = ImageOcr()
        img = FileNameUtils.join(self.path, "2.png")
        ocrResult = ocr.ocr(img, False)
        print(ocrResult)
        rectangle = ocr.getLeftTopAndRightBottomRectangle(ocrResult)
        draw = Imgage_Draw()
        thickness = 2
        print(rectangle)
        di = draw.rectangle(img,
                            [[rectangle[0][0] - thickness, rectangle[0][1] - thickness],
                             [rectangle[1][0] + thickness, rectangle[1][1] + thickness]])
        draw.showAndWait(di)

    def test_cropped(self):
        ocr = ImageOcr()
        img_path = FileNameUtils.join(self.path, "2.png")
        ocrResult = ocr.ocr(img_path, False)
        print(ocrResult)
        rectangle = ocr.getLeftTopAndRightBottomRectangle(ocrResult)
        draw = Imgage_Draw()
        thickness = 2
        print(rectangle)
        img = draw.imread(img_path)
        y1, y2 = int(rectangle[0][1] - thickness), int(rectangle[1][1] + thickness)
        x1, x2 = 0, img.shape[1]
        cropped = draw.crop(img, y1, y2, x1, x2)
        # cropped = img[y1:y2,x1:x2]
        draw.showAndWait(cropped)

    def create_img(self, img):
        return cv2.imread(FileNameUtils.join(self.path, img))

    def test_vconcat(self):
        # img1 = cv2.imread(FileNameUtils.join(self.path, "1.png"))
        # img2 = cv2.imread(FileNameUtils.join(self.path, "2.png"))
        # image_v = cv2.vconcat([img1, img2])
        draw = Imgage_Draw()
        # draw.showAndWait(image_v)
        # image = cv2.imread(FileNameUtils.join(self.path, "1.png"))
        # image2 = cv2.imread(FileNameUtils.join(self.path, "2.png"))
        # image_v = cv2.vconcat([image, image2])
        image_v = draw.vconcat_resize([self.create_img("1.png"), self.create_img("3.png")])
        r_v = cv2.resize(image_v, None, fx=0.5, fy=0.5)
        cv2.imshow("Result", r_v)
        cv2.waitKey(0)
        # cv2.imwrite(FileNameUtils.join(self.path, "image_v.png"), image_v)

    def test_join(self):
        sj = Screenshot_Join()
        image_v = sj.join_imgs([FileNameUtils.join(self.path, "1.png"), FileNameUtils.join(self.path, "2.png"),
                                FileNameUtils.join(self.path, "3.png"), FileNameUtils.join(self.path, "4.png"),
                                FileNameUtils.join(self.path, "5.png"), FileNameUtils.join(self.path, "6.png")],
                               top_thickness=15)
        r_v = cv2.resize(image_v, None, fx=0.5, fy=0.5)
        cv2.imshow("Result", r_v)
        cv2.waitKey(0)

    def test_join_and_save(self):
        sj = Screenshot_Join()
        sj.join_imgs_and_save([FileNameUtils.join(self.path, "1.png"), FileNameUtils.join(self.path, "2.png"),
                                         FileNameUtils.join(self.path, "3.png"), FileNameUtils.join(self.path, "4.png"),
                                         FileNameUtils.join(self.path, "5.png"),
                                         FileNameUtils.join(self.path, "6.png")],
                                        save_path=FileNameUtils.join(self.path, "image_v.png"),
                                        top_thickness=15)

    def test_s(self):
        a = ['a', 'b', 'c']
        print(a)
        b = a[1:]
        print(b)

    def test_splic(self):
        a = "a;b"
        print(a)
        b=a.split(";")
        print(b)

if __name__ == '__main__':
    unittest.main()
