class Solution(object):
    def movesToMakeZigzag(self, nums):
        nums = [float('inf')] + nums + [float('inf')]
        even_low, odd_low = 0, 0
        for i in range(1, len(nums) - 1):
            cost = max(0, nums[i] - min(nums[i - 1], nums[i + 1]) + 1)
            if i % 2 == 0:
                even_low += cost
            else:
                odd_low += cost
        return min(even_low, odd_low)
