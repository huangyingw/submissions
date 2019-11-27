class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        top_3 = nums[-1] * nums[-2] * nums[-3]
        top_bottom = nums[-1] * nums[0] * nums[1]
        return max(top_3, top_bottom)
