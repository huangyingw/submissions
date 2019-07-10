_author_ = 'jake'
_project_ = 'leetcode'










import math


class Solution(object):
    def reachNumber(self, target):

        target = abs(target)
        steps = int(math.ceil((math.sqrt(1 + 8 * target) - 1) / 2))
        target -= steps * (steps + 1) // 2
        if target % 2 == 0:
            return steps
        target += steps + 1
        if target % 2 == 0:
            return steps + 1
        return steps + 2
