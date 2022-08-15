# 电影截图拼接
import argparse
import fnmatch

from python_tools.utils.FileNameUtils import FileNameUtils
from python_tools.utils.StringUtils import StringUtils


class Screenshot_Join():
    def join(self, img_folder='./', img_list="", out="join_screenshot.png"):
        """
        电影截图拼接
        :param img_folder:
        :param img_list:
        :param out:
        :return:
        """
        imgs = self.getAllImg(img_folder, img_list)
        from python_tools.ocr.img_ocr import ImageOcr
        ocr = ImageOcr()
        ocrResult = ocr.ocrs(imgs, False)
        print(ocrResult)

    def getAllImg(self, img_folder, img_list):
        ret = []
        if (StringUtils.isNoEmpty(img_list)):
            ims = img_list.split(";")
            for im in ims:
                ret.append(FileNameUtils.join(img_folder, im))
        return ret


def parseArgument():
    parser = argparse.ArgumentParser(description='电影截图拼接')
    # type是要传入的参数的数据类型  help是该参数的提示信息
    parser.add_argument('--img_folder', type=str, help='图片文件',
                        default="./")
    parser.add_argument('--img_list', type=str, help='图片文件',
                        default="*.png")
    parser.add_argument('--out', type=str, help='图片文件',
                        default="join_screenshot.png")
    args = parser.parse_args()
    return args.img_path, args.img_list, args.out


if __name__ == "__main__":
    img_folder, img_list, out = parseArgument()
    iocr = Screenshot_Join()
    iocr.join(img_folder, img_list, out)
