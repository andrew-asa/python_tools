# 电影截图拼接
import argparse
import fnmatch

from python_tools.img.img_draw import Imgage_Draw
from python_tools.utils.FileNameUtils import FileNameUtils
from python_tools.utils.StringUtils import StringUtils


class Screenshot_Join():
    draw = None

    def __init__(self):
        self.draw = Imgage_Draw()

    def join_imgs(self, img_paths, top_thickness=2, bottom_thickness=2):
        from python_tools.ocr.img_ocr import ImageOcr
        ocr = ImageOcr()
        ocrResults = ocr.ocrs(img_paths, False)
        # draw = Imgage_Draw()
        base_img_path = img_paths[0]
        base_img = self.draw.imread(base_img_path)
        img_list = [base_img]
        concat_img_paths = img_paths[1:]
        for i in range(len(concat_img_paths)):
            concat_img = concat_img_paths[i]
            img_ocr_result = ocrResults[concat_img]
            rectangle = ocr.getLeftTopAndRightBottomRectangle(img_ocr_result)
            img = self.draw.imread(concat_img)
            y1, y2 = int(rectangle[0][1] - top_thickness), int(rectangle[1][1] + bottom_thickness)
            x1, x2 = 0, img.shape[1]
            cropped = self.draw.crop(img, y1, y2, x1, x2)
            img_list.append(cropped)
        return self.draw.vconcat_resize(img_list)

    def join_imgs_and_save(self, img_paths, save_path, top_thickness=2, bottom_thickness=2):
        img = self.join_imgs(img_paths, top_thickness, bottom_thickness)
        self.draw.imwrite(save_path, img)

    def join(self, img_folder, img_list, out, top_padding=2, bottom_padding=2):
        img_paths = []
        if StringUtils.isNoEmpty(img_list):
            str_list = img_list.split(";")
            for item in enumerate(str_list):
                img_paths.append(FileNameUtils.join(img_folder, item[1]))
            self.join_imgs_and_save(img_paths=img_paths, save_path=out, top_thickness=int(top_padding),
                                    bottom_thickness=int(bottom_padding))
        else:
            print("not found img_list")


def parseArgument():
    parser = argparse.ArgumentParser(description='电影截图拼接')
    # type是要传入的参数的数据类型  help是该参数的提示信息
    parser.add_argument('--img_folder', type=str, help='图片文件',
                        default="")
    parser.add_argument('--img_list', type=str, help='图片文件',
                        default="")
    parser.add_argument('--out', type=str, help='图片文件',
                        default="join_screenshot.png")
    parser.add_argument('--top_padding', type=int, help='弹幕上方距离',
                        default=5)
    parser.add_argument('--bottom_padding', type=int, help='弹幕下方距离',
                        default=2)
    args = parser.parse_args()
    return args.img_path, args.img_list, args.out, args.top_padding, args.bottom_padding


if __name__ == "__main__":
    img_folder, img_list, out, top_padding, bottom_padding = parseArgument()
    sj = Screenshot_Join()
    sj.join_imgs_and_save(img_list, save_path=out, top_thickness=top_padding, bottom_padding=bottom_padding)
