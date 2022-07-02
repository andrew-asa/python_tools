import time


def getYY_MM_DD():
    """
    获取yymmdd字符串
    :return:
    """
    return time.strftime("%Y-%m-%d", time.localtime())



def get_date_str(format="%Y-%m-%d"):
    """
    获取时间字符串

    :param format: %Y-%m-%d %H:%M:%S 类似字符
    :return: 格式化之后的字符串
    """
    return time.strftime(format, time.localtime())
