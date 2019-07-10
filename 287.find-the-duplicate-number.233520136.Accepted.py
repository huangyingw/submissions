_author_ = 'jake'
_project_ = 'leetcode'














class Solution(object):
    def findDuplicate(self, nums):

        slow = nums[0]
        fast = nums[slow]
        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
        return fast
