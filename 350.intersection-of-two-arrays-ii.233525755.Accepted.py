_author_ = 'jake'
_project_ = 'leetcode'








from collections import Counter


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        freq1 = Counter(nums1)
        result = []
        for i, num in enumerate(nums2):
            if num in freq1 and freq1[num] > 0:
                freq1[num] -= 1
                result.append(num)
        return result
