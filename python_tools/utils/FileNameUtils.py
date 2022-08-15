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
    def dirname(path):
        """
        返回路径中的目录部分
        :return:
        """
        return os.path.dirname(path)
    def base_name(path):
        return os.path.basename(path)