_author_ = 'jake'
_project_ = 'leetcode'








class Solution(object):
    def findMaxConsecutiveOnes(self, nums):

        consecutive, max_consecutive = 0, 0
        for num in nums:
            if num == 0:
                max_consecutive = max(max_consecutive, consecutive)
                consecutive = 0
            else:
                consecutive += 1
        return max(max_consecutive, consecutive)
