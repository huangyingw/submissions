_author_ = 'jake'
_project_ = 'leetcode'







class Solution(object):
    def intersection(self, nums1, nums2):

        return list(set(nums1) & set(nums2))
