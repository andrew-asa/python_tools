import os
import shutil

from python_tools.utils.FileNameUtils import FileNameUtils


class FileUtils:
    """
    文件操作工具类
    """

    def emptyDir(path):
        """
        清空文件夹
        :return:
        """
        shutil.rmtree(path)
        os.mkdir(path)

    def isFile(path):
        """
        是否是文件
        :return:
        """
        return os.path.isfile(path)

    def isDir(path):
        """
        是否是文件夹
        :return:
        """
        return os.path.isdir(path)

    def exists(path):
        """
        文件是否存在
        :return:
        """
        return os.path.exists(path)



    def makeSureDirExist(path):
        """
        确保父文件夹位置存在
        :return:
        """

        dirname = FileNameUtils.dirname(path)
        if not FileUtils.exists(dirname):
            os.mkdir(dirname)

    def mkdir(path):
        """
        创建目录
        :return:
        """
        if not FileUtils.exists(path):
            os.mkdir(path)
