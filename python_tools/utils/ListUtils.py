# join 二维列表
EMPTY_LIST = []


class ListUtils:
    def isEmptyList(list):
        """
        列表是否为空
        :return:
        """
        return list == EMPTY_LIST

    def isNoEmptyList(list):
        """
        列表是否非空
        :return:
        """
        return not ListUtils.isEmptyList(list)

    def joinTwoDimensionList(result=[], sequence="", lineSequence="\n"):
        """
        二维数组字符串join
        :param sequence: 一维拼接符
        :param lineSequence: 维之间拼接符
        :return: 拼接的字符串 ([['上','下'],['左','右']],"","\n") => 上下\n左右
        """
        lines = []
        if (ListUtils.isNoEmptyList(result)):
            for line in result:
                lines.append(sequence.join(line))
        return lineSequence.join(lines)
