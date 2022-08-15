import argparse
import tempfile

from paddleocr import PPStructure, draw_structure_result, save_structure_res, PaddleOCR, draw_ocr
import functools

from python_tools.utils.DateUtils import DateUtils
from python_tools.utils.FileNameUtils import FileNameUtils
from python_tools.utils.IOUtils import IOUtils
from python_tools.utils.ListUtils import *
from python_tools.utils.ClipboardUtils import *
from python_tools.utils.StringUtils import StringUtils


class ImageOcr():
    # 行扫描的大概范围
    same_line_rang = 8
    default_clipboard_save_path = "~/"

    def set_default_clipboard_save_path(self, path):
        if (StringUtils.isNoEmpty(path)):
            self.default_clipboard_save_path = path

    def set_same_line_rang(self, rang):
        self.same_line_rang = rang;

    def sameLine(self, point1, point2, loss=same_line_rang):
        y1, y2 = point1[1], point2[1]
        return abs(y1 - y2) <= loss

    def noSameLine(self, point1, point2, loss):
        return not self.sameLine(point1, point2, loss)

    def getResultLineContent(self, line):
        return line[1][0]

    def joinResultString(self, result=[], sequence=""):
        s = []
        for line in result:
            s.append(self.getResultLineContent(line))
        return sequence.join(s)

    # 获取左上角的点
    def getTopLeftCornerPoint(self, line):
        return line[0][0];

    # 扫描已经排序过的结果
    def scanOrderResult(self, result, loss=8):
        ret = [];
        current = []
        currentPoint = [0, 0]
        for line in result:
            tlc = self.getTopLeftCornerPoint(line)
            if (not self.sameLine(currentPoint, tlc, loss)):
                if (len(current) > 0):
                    ret.append(current)
                currentPoint = tlc
                current = []
            current.append(self.getResultLineContent(line))
        if (len(current) > 0):
            ret.append(current)
        return ret

    def ocrPointCompare(self, line1, line2):
        point1 = line1[0][0]
        point2 = line2[0][0]
        x1, y1 = point1[0], point1[1]
        x2, y2 = point2[0], point2[1]
        if (self.sameLine(point1, point2)):
            if (x1 == x2):
                return 0
            elif (x1 < x2):
                return -1
        elif (y1 < y2):
            return -1
        return 1

    def sortOcrResult(self, result):
        result.sort(key=functools.cmp_to_key(self.ocrPointCompare))

    def ocrs(self, img_paths=[], sortResult=True):
        """
        多个图片ocr
        :param img_paths:
        :param sortResult:
        :return:
        """
        ret = {}
        for img in img_paths:
            ret[img] = self.ocr(img, sortResult)
        return ret

    def ocr(self, img_path, sortResult=True):
        """
        图片ocr
        :param img_path:
        :param sortResult: 如果为false则返回的是PaddleOcr的原始结果
                           默认则返回整理过后的二维数组
        :return:
        """
        ocr = PaddleOCR(use_angle_cls=True, use_gpu=False);
        result = ocr.ocr(img_path, cls=True)
        if (sortResult):
            self.sortOcrResult(result)
            return self.scanOrderResult(result)
        return result

    def img_ocr(self, img_path, print_in_console=True, copy_to_clipboard=True, colSequence=" ", rowSequence="\n"):
        """
        图片ocr识别
        :param img_path: 图片路径
        :param print_in_console: 是否在控制台打印识别信息
        :param copy_to_clipboard: 是否复制识别的文字到粘贴板
        :param sequence: 列之间的间隔符
        :param lineSequence: 行之间的间隔符
        :return:
        """
        ret = self.ocr(img_path)
        content = ListUtils.joinTwoDimensionList(ret, colSequence, rowSequence)
        if (print_in_console):
            print("-- img ocr result --")
            print(content)
            print("-- img ocr result --")
        if (copy_to_clipboard):
            ClipboardUtils.copyToClipboard(content)
        return content

    def __create_temp_img_path(self):
        fn = DateUtils.get_date_str("%Y-%m-%d-%H-%M-%S") + ".png"
        tempdir = tempfile.gettempdir()
        save_img_path = FileNameUtils.join(tempdir, fn)
        return save_img_path

    def ocr_clipboard_img(self, save_img_path="",
                          print_in_console=True,
                          copy_to_clipboard=True,
                          delete_after_ocr=True,
                          colSequence=" ",
                          rowSequence="\n"):
        """
        ocr识别站粘贴板中的图片文字
        :param save_img_path:
        :param copy_to_clipboard:
        :return:
        """
        content = ""
        if (StringUtils.isEmpty(save_img_path)):
            save_img_path = self.__create_temp_img_path()
        if (ClipboardUtils.copyImageTo(save_img_path)):
            print("save img to ", save_img_path)
            content = self.img_ocr(img_path=save_img_path,
                                   print_in_console=print_in_console,
                                   copy_to_clipboard=copy_to_clipboard,
                                   colSequence=colSequence,
                                   rowSequence=rowSequence)
            if (delete_after_ocr):
                IOUtils.deleteFile(save_img_path)
        else:
            print("粘贴板上没有图片")
        return content


def parseArgument():
    parser = argparse.ArgumentParser(description='表格OCR')
    # type是要传入的参数的数据类型  help是该参数的提示信息
    parser.add_argument('--img_path', type=str, help='表格图片文件',
                        default="/Users/andrew_asa/Documents/code/github/andrew-asa/exec/python/python_tools/res/img-20220623072555.png")
    args = parser.parse_args()
    return args.img_path


if __name__ == "__main__":
    img_path, save_folder = parseArgument()
    print("img_path=" + img_path)
    iocr = ImageOcr()
    iocr.img_ocr(img_path)
