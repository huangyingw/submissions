_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def findMaxConsecutiveOnes(self, nums):

        max_consecutive = 0
        i = 0
        while i < len(nums) and nums[i] == 0:
            i += 1
        start, prev_start = i, max(i - 1, 0)
        for j in range(i + 1, len(nums)):
            if nums[j] == 0:
                if j != 0 and nums[j - 1] == 0:
                    prev_start = j
                else:
                    max_consecutive = max(max_consecutive, j - prev_start)
                    prev_start = start
                start = j + 1
        return max(max_consecutive, len(nums) - prev_start)
