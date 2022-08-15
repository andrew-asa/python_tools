if __name__ == '__main__':
    from python_tools.ocr.img_ocr import ImageOcr
    from python_tools.utils.ClipboardUtils import ClipboardUtils
    from python_tools.utils.StringUtils import StringUtils

    content = self.ocr.ocr_clipboard_img(print_in_console=False, copy_to_clipboard=False, colSequence=" | ",
                                         rowSequence=" |\n| ")
    if (StringUtils.isNoEmpty(content)):
        content = "| " + content + " |"
        ClipboardUtils.copyToClipboard(content)
    print("--ocr result --")
    print(content)
    print("--ocr result --")