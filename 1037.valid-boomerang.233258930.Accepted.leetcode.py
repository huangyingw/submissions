_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if len({tuple(point) for point in points}) != 3:
            return False
        dx_1 = points[1][0] - points[0][0]
        dy_1 = points[1][1] - points[0][1]
        dx_2 = points[2][0] - points[0][0]
        dy_2 = points[2][1] - points[0][1]
        return dy_1 * dx_2 != dy_2 * dx_1
