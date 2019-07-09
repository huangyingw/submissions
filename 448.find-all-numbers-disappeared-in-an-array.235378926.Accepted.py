_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            num = abs(num)
            nums[num - 1] = -abs(nums[num - 1])
        return [i + 1 for i, num in enumerate(nums) if num > 0]
