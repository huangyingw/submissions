class Solution:
    def solve(self, nums, queries):
        MOD = 10**9 + 7
        MAX_NUMS = 10**5 + 10
        MAX_Y = 100 + 10
        n = len(nums)
        prefix_sums = [[0] * MAX_Y for _ in range(MAX_NUMS)]
        for i in range(n):
            for j in range(1, MAX_Y):
                prefix_sums[i + 1][j] = (
                    prefix_sums[i + 1][j] + prefix_sums[i][j]
                ) % MOD
                if i % j == 0:
                    prefix_sums[i + 1][j] = (
                        prefix_sums[i + 1][j] + nums[i]
                    ) % MOD
        result = []
        for xi, yi in queries:
            total = (prefix_sums[n][yi] - prefix_sums[xi][yi] + nums[xi]) % MOD
            result.append(total)
        return result
