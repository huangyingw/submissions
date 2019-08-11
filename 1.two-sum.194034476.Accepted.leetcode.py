class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for idx, val in enumerate(nums):
            if target - val in dict:
                return (dict[target - val], idx)
            dict[val] = idx
