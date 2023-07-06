class Solution:
    def solve(self, nums, queries):
        MOD = 10**9 + 7
        n = len(nums)
        sums = {}
        result = []
        for xi, yi in queries:
            if (xi, yi) not in sums:
                j = xi
                total = 0
                while j < n:
                    total += nums[j]
                    j += yi
                sums[(xi, yi)] = total % MOD
            result.append(sums[(xi, yi)])
        return result
