_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, candidate = 0, None
        for i, num in enumerate(nums):
            if count == 0:
                candidate = num
            if candidate == num:
                count += 1
            else:
                count -= 1
        return candidate
