_author_ = 'jake'
_project_ = 'leetcode'








import math


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(1 + 8.0 * n) - 1) / 2
