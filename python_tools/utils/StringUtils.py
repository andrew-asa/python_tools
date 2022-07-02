class StringUtils:
    def isEmpty(str=""):
        return len(str) == 0

    def isNoEmpty(str=""):
        """
        字符串是否非空
        :return:
        """
        return not StringUtils.isEmpty(str)
