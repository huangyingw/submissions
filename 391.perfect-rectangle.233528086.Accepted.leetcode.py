from collections import defaultdict
class Solution(object):
    def isRectangleCover(self, rectangles):
        min_r, min_c = float("inf"), float("inf")
        max_r, max_c = float("-inf"), float("-inf")
        area = 0
        corners = defaultdict(int)
        for r1, c1, r2, c2 in rectangles:
            area += (r2 - r1) * (c2 - c1)
            min_r = min(min_r, r1)
            min_c = min(min_c, c1)
            max_r = max(max_r, r2)
            max_c = max(max_c, c2)
            corners[(r1, c1)] += 1
            corners[(r2, c2)] += 1
            corners[(r1, c2)] += 1
            corners[(r2, c1)] += 1
        rows = max_r - min_r
        cols = max_c - min_c
        if area != rows * cols:
            return False
        for r, c in corners:
            if r in {min_r, max_r} and c in {min_c, max_c}:
                if corners[(r, c)] != 1:
                    return False
            elif corners[(r, c)] % 2 != 0:
                return False
        return True
