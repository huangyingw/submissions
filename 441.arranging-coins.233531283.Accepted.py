







import math


class Solution(object):
    def arrangeCoins(self, n):

        return int(math.sqrt(1 + 8.0 * n) - 1) / 2
