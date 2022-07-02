import functools


class CompareUtils:
    """
    比较工具类
    """
    def coordinateCompare(obj1, obj2):
        """
        坐标比较,左上，右下的位置比较
        :param obj2:
        :return:
        """
        x1, y1 = obj1[0], obj1[1]
        x2, y2 = obj2[0], obj2[1]
        if (y1 < y2):
            return -1
        elif (y1 == y2):
            if (x1 == x2):
                return 0
            elif (x1 < x2):
                return -1
        return 1
        # print('[{},{}][{},{}]'.format(x1,y1,x2,y2))

    def coordinateSort(points):
        """
        坐标排序
        :return:
        """
        return points.sort(key=functools.cmp_to_key(CompareUtils.coordinateCompare))
