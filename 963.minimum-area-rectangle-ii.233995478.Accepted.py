










from collections import defaultdict
from itertools import combinations


class Solution(object):
    def minAreaFreeRect(self, points):

        min_area = float("inf")
        points = [complex(*p) for p in sorted(points)]
        line_to_mid = defaultdict(list)
        for p1, p2 in combinations(points, 2):
            line_to_mid[p2 - p1].append((p1 + p2) / 2)
        for line1, mid_points in line_to_mid.items():
            for mid1, mid2 in combinations(mid_points, 2):
                line2 = mid2 - mid1
                if line1.real * line2.real + line1.imag * line2.imag == 0:
                    min_area = min(min_area, abs(line1) * abs(line2))
        return min_area if min_area != float("inf") else 0
