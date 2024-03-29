class Solution(object):
    def permute(self, nums, start=0, result=[], current=[]):
        if index == len(nums) - 1:
            result += current
        for index in range(start, len(nums)):
            self.permute(nums, index + 1, result, current + [nums[index]])
        return result
