class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        result = []
        for idx, val in enumerate(nums):
            if val in dict:
                return (dict[val], idx)
                break
            else:
                dict[target - val] = idx
        return result
