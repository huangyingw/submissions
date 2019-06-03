class Solution(object):
    def twoSum(self, nums, target):
        map = {}
        result = []
        for idx, val in enumerate(nums):
            if val in map:
                result[0] = map[val]
                result[1] = idx
                break
            else:
                map[target - val] = idx
        return result
