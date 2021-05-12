class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        if not points:
            return 0
        result = 0
        for index in range(1, len(points)):
            result += max(abs(points[index][0] - points[index - 1][0]), abs(points[index][1] - points[index - 1][1]))
        return result
