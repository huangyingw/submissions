_author_ = 'jake'
_project_ = 'leetcode'














import bisect


class RangeModule(object):
    def __init__(self):
        self.points = [0, 10 ** 9]
        self.in_range = [False, False]

    def addRange(self, left, right, add=True):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        i = bisect.bisect_left(self.points, left)
        if self.points[i] != left:
            self.points.insert(i, left)
            self.in_range.insert(i, self.in_range[i - 1])
        j = bisect.bisect_left(self.points, right)
        if self.points[j] != right:
            self.points.insert(j, right)
            self.in_range.insert(j, self.in_range[j - 1])
        self.points[i:j] = [left]
        self.in_range[i:j] = [add]

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        i = bisect.bisect(self.points, left) - 1
        j = bisect.bisect_left(self.points, right)
        return all(self.in_range[i:j])

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        self.addRange(left, right, False)
