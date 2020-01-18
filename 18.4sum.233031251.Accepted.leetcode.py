class Solution(object):
    def fourSum(self, nums, target):
        sumMapping = {}
        for index_i in range(len(nums) - 1):
            for index_j in range(index_i + 1, len(nums)):
                currSum = nums[index_i] + nums[index_j]
