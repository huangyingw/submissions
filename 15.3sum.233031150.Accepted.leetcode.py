class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        if (len(nums) >= 3) and (nums[0] == nums[len(nums) - 1]) and (nums[0] == 0):
            return [[0, 0, 0]]
        result = []
        for index in range(len(nums) - 1):
            left = index + 1
