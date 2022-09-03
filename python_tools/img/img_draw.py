import cv2


class Imgage_Draw():
    def rectangle(self, img, rec, color=(0, 255, 0), thickness=2):
        """
        添加矩形
        :param img:
        :param rec:
        :param color:
        :param thickness:
        :return:
        """

        image = cv2.imread(img)
        x1, y1, x2, y2 = int(rec[0][0]), int(rec[0][1]), int(rec[1][0]), int(rec[1][1])
        draw = cv2.rectangle(image, pt1=(x1, y1), pt2=(x2, y2), color=color, thickness=thickness)
        # draw = cv2.rectangle(image, (rec[0][0], rec[0][1]), (rec[1][0], rec[1][1]), color, thickness)
        return draw

    def imread(self, filename):
        """
        文件名转图像
        :param filename:
        :return:
        """
        return cv2.imread(filename)

    def imwrite(self, filename, img):
        """
        图像转文件
        :param filename:
        :param img:
        :return:
        """
        cv2.imwrite(filename, img)

    def showAndWait(self, img, winName="imshow"):
        cv2.imshow(winName, img)
        cv2.waitKey(0)
        cv2.destroyWindow(winName)

    def vconcat_resize(self, img_list, interpolation=cv2.INTER_CUBIC):
        """
        垂直拼接
        :param img_list:
        :param interpolation:
        :return:
        """
        # take minimum width

        w_min = min(img.shape[1]

                    for img in img_list)

        # resizing images

        im_list_resize = [cv2.resize(img,

                                     (w_min, int(img.shape[0] * w_min / img.shape[1])),

                                     interpolation=interpolation)

                          for img in img_list]

        return cv2.vconcat(im_list_resize)

    def hconcat_resize(self, img_list, interpolation=cv2.INTER_CUBIC):
        """
        水平拼接
        :param interpolation:
        :return:
        """
        # take minimum hights
        h_min = min(img.shape[0]

                    for img in img_list)

        # image resizing

        im_list_resize = [cv2.resize(img,

                                     (int(img.shape[1] * h_min / img.shape[0]),

                                      h_min), interpolation

                                     =interpolation)

                          for img in img_list]

        # return final image

        return cv2.hconcat(im_list_resize)

    def crop(self, img, y1, y2, x1, x2):
        """
        裁剪
        :param img:
        :param y1:
        :param y2:
        :param x1:
        :param x2:
        :return:
        """
        return img[int(y1):int(y2), int(x1):int(x2)]
