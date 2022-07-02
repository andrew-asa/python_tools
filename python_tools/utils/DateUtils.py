import time


class DateUtils:
    """
    时间相关工具类
    """
    yy_mm_dd = "%Y-%m-%d"
    hh_mm_ss = "%H:%M:%S"
    yy_mm_dd_hh_mm_ss = "%Y-%m-%d %H:%M:%S"

    def getYY_MM_DD(p=""):
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
