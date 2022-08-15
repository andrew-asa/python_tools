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

    def endswith(str, endStr):
        """
        str是否以endStr结尾
        :param endStr:
        :return:
        """
        return StringUtils.isNoEmpty(str) and str.endswith(endStr)

    def equal(str1,str2):
        """
        字符串是否相等
        :param str2:
        :return:
        """
        return  str1 == str2
