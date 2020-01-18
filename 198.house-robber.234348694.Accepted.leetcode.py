class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        current, prev = nums[0], 0
        for i in nums[1:]:
            prev, current = current, max(prev + i, current)
        return current
