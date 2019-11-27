class Solution:
    def twoSum(self, nums, target):
        pair = {}
        for i in range(len(nums)):
            if nums[i] in pair.keys():
                return [pair.get(nums[i]), i]
            else:
                pair[target - nums[i]] = i
        return []
