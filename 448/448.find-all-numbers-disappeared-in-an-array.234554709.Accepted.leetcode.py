class Solution(object):
    def findDisappearedNumbers(self, nums):
        temp = [0] * len(nums)
        for i in range(len(nums)):
            temp[nums[i] - 1] = 1
        return [i + 1 for i in range(0, len(nums)) if not temp[i]]
