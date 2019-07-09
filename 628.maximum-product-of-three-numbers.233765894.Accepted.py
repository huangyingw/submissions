_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        top_3 = nums[-1] * nums[-2] * nums[-3]
        top_bottom = nums[-1] * nums[0] * nums[1]
        return max(top_3, top_bottom)
