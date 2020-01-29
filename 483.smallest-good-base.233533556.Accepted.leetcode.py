import math


class Solution(object):
    def smallestGoodBase(self, n):
        n = int(n)
        for max_power in range(int(math.log(n, 2)), 1, -1):
            base = int(n ** max_power ** -1)
            if n == ((base ** (max_power + 1)) - 1) // (base - 1):
                return str(base)
        return str(n - 1)
