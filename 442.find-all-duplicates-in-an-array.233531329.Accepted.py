_author_ = 'jake'
_project_ = 'leetcode'








class Solution(object):
    def findDuplicates(self, nums):

        result = []
        for i in range(len(nums)):
            num = abs(nums[i])
            if nums[num - 1] < 0:
                result.append(num)
                continue
            nums[num - 1] = -nums[num - 1]
        return result
