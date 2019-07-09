_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        points.append(points[0])
        points.append(points[1])
        previous = [points[1][0] - points[0][0], points[1][1] - points[0][1]]
        previous_cross = 0
        for i in range(2, len(points)):
            vector = [points[i][0] - points[i - 1][0], points[i][1] - points[i - 1][1]]
            cross_product = vector[0] * previous[1] - vector[1] * previous[0]
            if cross_product != 0:
                if previous_cross * cross_product < 0:
                    return False
                previous_cross = cross_product
            previous = vector
        return True
