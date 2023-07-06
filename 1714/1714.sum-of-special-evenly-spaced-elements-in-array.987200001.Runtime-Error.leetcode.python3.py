class Solution:
    def solve(self, nums, queries):
        MOD = 10**9 + 7
        n = len(nums)
        dp = [[0] * 101 for _ in range(n + 1)]
        for yi in range(1, 101):
            dp[n - 1][yi] = nums[n - 1]
            for xi in range(n - 2, -1, -1):
                if xi + yi < n:
                    dp[xi][yi] = (dp[xi + yi][yi] + nums[xi]) % MOD
                else:
                    dp[xi][yi] = nums[xi]
        result = []
        for xi, yi in queries:
            result.append(dp[xi][yi])
        return result
