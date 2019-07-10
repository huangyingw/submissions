_author_ = 'jake'
_project_ = 'leetcode'







class Solution(object):
    def findLengthOfLCIS(self, nums):

        longest, current = 0, 0
        for i, num in enumerate(nums):
            if i == 0 or num <= nums[i - 1]:
                current = 0
            current += 1
            longest = max(longest, current)
        return longest
