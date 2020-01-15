from collections import defaultdict


class Solution(object):
    def isReflected(self, points):
        y_to_x = defaultdict(set)
        for x, y in points:
            y_to_x[y].add(x)
        reflection = None
        for y in y_to_x:
            xs = sorted(list(y_to_x[y]))
            left, right = 0, len(xs) - 1
            if reflection is None:
                reflection = xs[left] + xs[right]
                left += 1
                right -= 1
            while left <= right:
                if xs[right] + xs[left] != reflection:
                    return False
                left += 1
                right -= 1
        return True
