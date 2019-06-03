class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for idx, val in enumerate(nums):
            if val in dict:
                return (dict[val], idx)
            else:
                dict[target - val] = idx
