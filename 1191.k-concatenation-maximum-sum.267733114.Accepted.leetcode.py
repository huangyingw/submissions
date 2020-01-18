class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        MOD = 10 ** 9 + 7
        total = sum(arr)
        max_prefix, max_end_here, max_subarray = 0, 0, 0
        cumulative = 0
        for a in arr:
            cumulative += a
            max_prefix = max(max_prefix, cumulative)
            max_end_here = max(max_end_here, 0) + a
            max_subarray = max(max_subarray, max_end_here)
        max_suffix = 0
        cumulative = 0
        for a in arr[::-1]:
            cumulative += a
            max_suffix = max(max_suffix, cumulative)
        if k == 1:
            return max_subarray % MOD
        return max(max_subarray, max_prefix + max_suffix + max(total, 0) * (k - 2)) % MOD
