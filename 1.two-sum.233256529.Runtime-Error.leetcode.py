class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        result = []
        for idx, val in enumerate(nums):
            if val in dict:
                result[0] = dict[val]
                result[1] = idx
                break
            else:
                dict[target - val] = idx
        return result
