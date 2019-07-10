_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def containsDuplicate(self, nums):

        return len(set(nums)) != len(nums)
