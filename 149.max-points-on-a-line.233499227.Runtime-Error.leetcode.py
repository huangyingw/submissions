class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
from collections import defaultdict
class Solution(object):
    def maxPoints(self, points):
        if len(points) <= 2:
            return len(points)
        overall_max = 2
        for i, point in enumerate(points):
            gradients = defaultdict(int)
            max_points = 1
            for point_2 in points[i + 1:]:
                if point.x == point_2.x:
                    if point.y == point_2.y:
                        max_points += 1
                    else:
                        gradients['inf'] += 1
                else:
                    gradient = (point_2.y - point.y) / float(point_2.x - point.x)
                    gradients[gradient] += 1
            if gradients:
                max_points += max(gradients.values())
            overall_max = max(overall_max, max_points)
        return overall_max
