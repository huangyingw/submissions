class Solution(object):
    def permute(self, nums):
        result = []
        for index in range(len(nums)):
            for p in self.permute(nums[0:index] + nums[index + 1:]):
                result.append([nums[index]] + p)
        return result
