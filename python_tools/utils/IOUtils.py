import io
import os
from pathlib import Path

from python_tools.utils.StringUtils import StringUtils


class IOUtils:
    """
    IO相关操作
    """
    def deleteFile(fn):
        """
        删除文件
        :return:
        """
        if(StringUtils.isNoEmpty(fn)):
            os.remove(fn)
