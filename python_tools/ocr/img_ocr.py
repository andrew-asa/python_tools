import argparse
from paddleocr import PPStructure, draw_structure_result, save_structure_res, PaddleOCR, draw_ocr
import functools
from python_tools.utils.ListUtils import *
from python_tools.utils.ClipboardUtils import *


def sameLine(point1, point2, loss=8):
    y1, y2 = point1[1], point2[1]
    return abs(y1 - y2) <= loss


def noSameLine(point1, point2, loss):
    return not sameLine(point1, point2, loss)


def getResultLineContent(line):
    return line[1][0]


def joinResultString(result=[], sequence=""):
    s = []
    for line in result:
        s.append(getResultLineContent(line))
    return sequence.join(s)


# 获取左上角的点
def getTopLeftCornerPoint(line):
    return line[0][0];


# 扫描已经排序过的结果
def scanOrderResult(result, loss=8):
    ret = [];
    current = []
    currentPoint = [0, 0]
    for line in result:
        tlc = getTopLeftCornerPoint(line)
        if (not sameLine(currentPoint, tlc, loss)):
            if (len(current) > 0):
                ret.append(current)
            currentPoint = tlc
            current = []
        current.append(getResultLineContent(line))
    if (len(current) > 0):
        ret.append(current)
    return ret

def ocrPointCompare(line1, line2):
    point1 = line1[0][0]
    point2 = line2[0][0]
    x1, y1 = point1[0], point1[1]
    x2, y2 = point2[0], point2[1]
    if (sameLine(point1, point2)):
        if (x1 == x2):
            return 0
        elif (x1 < x2):
            return -1
    elif (y1 < y2):
        return -1
    return 1


def sortOcrResult(result):
    result.sort(key=functools.cmp_to_key(ocrPointCompare))


def parseArgument():
    parser = argparse.ArgumentParser(description='表格OCR')
    # type是要传入的参数的数据类型  help是该参数的提示信息
    parser.add_argument('--img_path', type=str, help='表格图片文件',
                        default="/Users/andrew_asa/Documents/code/github/andrew-asa/exec/python/python_tools/res/img-20220623072555.png")
    parser.add_argument('--save_folder', type=str, help='输出路径', default="/Users/andrew_asa/temp/ocr/out")
    args = parser.parse_args()
    return args.img_path, args.save_folder


def img_ocr(img_path, save_folder):
    ocr = PaddleOCR(use_angle_cls=True, use_gpu=False);
    result = ocr.ocr(img_path, cls=True);
    # result.sort()
    sortOcrResult(result)
    ret = scanOrderResult(result)
    content = ListUtils.joinTwoDimensionList(ret," ")
    print(content)
    ClipboardUtils.copyToClipboard(content)
    # print(ret)
    # for line in result:
    #     print(line);


if __name__ == "__main__":
    img_path, save_folder = parseArgument()
    print("img_path=" + img_path)
    print("save_folder=" + save_folder)
    img_ocr(img_path, save_folder)
