_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def removeDuplicates(self, nums):

        next = 2
        for index in range(2, len(nums)):
            if nums[index] != nums[next - 2]:
                nums[next] = nums[index]
                next += 1
        return min(next, len(nums))
