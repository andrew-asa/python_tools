import pyperclip
from PIL import Image, ImageGrab


class ClipboardUtils:

    # 复制文本到粘贴板
    def copyToClipboard(text=""):
        pyperclip.copy(text)

    # 从粘贴板中复制文本
    def copyFromClipboard(p=""):
        return pyperclip.paste()

    def copyImageTo(dest=""):
        im = ImageGrab.grabclipboard();
        if isinstance(im, Image.Image):
            im.save(dest)
        return
