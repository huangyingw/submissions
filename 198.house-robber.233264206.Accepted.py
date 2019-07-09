_author_ = 'jake'
_project_ = 'leetcode'












class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        loot, prev = nums[0], 0
        for num in nums[1:]:
            loot, prev = max(num + prev, loot), loot
        return loot
