class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        t = [1] + [0] * n
        for i in nums:
            if i >= 1 and i <= n:
                t[i] = 1
        j = 1
        while j <= n:
            if t[j] == 0:
                return j
            j += 1
        return n + 1
