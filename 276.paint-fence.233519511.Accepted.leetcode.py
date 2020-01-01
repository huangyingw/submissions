class Solution(object):
    def numWays(self, n, k):
        if n == 0:
            return 0
        if n == 1:
            return k
        same, different = 0, k
        for _ in range(n - 1):
            same, different = different, (same + different) * (k - 1)
        return same + different