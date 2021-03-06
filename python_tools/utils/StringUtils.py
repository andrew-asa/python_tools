class StringUtils:
    """
    字符串操作工具类
    """
    def isEmpty(str=""):
        """
        字符串判空
        :return:
        """
        return len(str) == 0

    def isNoEmpty(str=""):
        """
        字符串是否非空
        :return:
        """
        return not StringUtils.isEmpty(str)
