import pyperclip
from PIL import Image, ImageGrab


class ClipboardUtils:
    """
    粘贴板工具类
    """
    def copyToClipboard(text=""):
        """
        复制文本到粘贴板
        :return:
        """
        pyperclip.copy(text)

    def copyFromClipboard(p=""):
        """
        从粘贴板中复制文本
        :return:
        """
        return pyperclip.paste()

    def copyImageTo(dest=""):
        """
        粘贴板图片保存
        :return:
        """
        im = ImageGrab.grabclipboard();
        if isinstance(im, Image.Image):
            im.save(dest)
            return  True
        else:
            print("clipboard no contain img ")
        return False
