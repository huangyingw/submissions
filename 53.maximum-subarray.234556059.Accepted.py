


class Solution(object):
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0
        Sum = nums[0]
        result = Sum
        for i in range(1, len(nums)):
            Sum = (Sum + nums[i]) if(Sum + nums[i]) >= nums[i] else nums[i]
            result = Sum if Sum > result else result
        return result
