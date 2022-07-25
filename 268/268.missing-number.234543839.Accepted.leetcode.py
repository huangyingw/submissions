class Solution:

    def missingNumber(self, nums):

        for i in range(len(nums) + 1):
            if i not in nums:
                return i

    def missingNumber(self, nums):

        s = set(nums)
        for i in range(len(nums) + 1):
            if i not in s:
                return i

    def missingNumber(self, nums):

        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)
