_author_ = 'jake'
_project_ = 'leetcode'








import random
import bisect


class Solution(object):
    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.cumulative = []
        total = 0
        for weight in w:
            total += weight
            self.cumulative.append(total)

    def pickIndex(self):
        """
        :rtype: int
        """
        x = random.randint(1, self.cumulative[-1])
        return bisect.bisect_left(self.cumulative, x)
