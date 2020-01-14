import functools
class Solution:
    def mergeStones(self, stones, K):
        n = len(stones)
        if (n - 1) % (K - 1) != 0:
            return -1
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + stones[i]
        @functools.lru_cache(None)
        def helper(i, j):
            if j - i + 1 < K:
                return 0
            res = min(helper(i, mid) + helper(mid + 1, j) for mid in range(i, j, K - 1))
            if (j - i) % (K - 1) == 0:
                res += prefix_sum[j + 1] - prefix_sum[i]
            return res
        return helper(0, n - 1)
