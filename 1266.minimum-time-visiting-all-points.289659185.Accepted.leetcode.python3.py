class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        x1, y1 = points[0]
        time = 0
        for x2, y2 in points[1:]:
            dx, dy = abs(x1 - x2), abs(y1 - y2)
            time += max(dx, dy)
            x1, y1 = x2, y2
        return time
