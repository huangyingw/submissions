class Solution:
    def solve(self, nums, queries):
        MOD = 10**9 + 7
        result = []
        for xi, yi in queries:
            total = sum(nums[j] for j in range(xi, len(nums), yi))
            result.append(total % MOD)
        return result
