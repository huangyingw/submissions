class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution(object):
    def outerTrees(self, points):
        if len(points) < 3:
            return points

        def slope(a, b):
            if a.x == b.x:
                return float("inf")
            return (b.y - a.y) / float(b.x - a.x)

        def cross_product(p):
            v1 = [result[-1].x - result[-2].x, result[-1].y - result[-2].y]
            v2 = [p.x - result[-2].x, p.y - result[-2].y]
            return v1[0] * v2[1] - v1[1] * v2[0]
        start_point = min(points, key=lambda p: (p.x, p.y))
        points.remove(start_point)
        points.sort(key=lambda p: (slope(start_point, p), -p.y, p.x))
        result = [start_point, points[0]]
        for point in points[1:]:
            while cross_product(point) < 0:
                result.pop()
            result.append(point)
        return result
