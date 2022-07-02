import os


class FileNameUtils:
    """
    文件名操作工具类
    """

    def join(basePath, *p):
        """
        路径拼接
        :param subPath:
        :return:
        """
        return os.path.join(basePath, *p)
