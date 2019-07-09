_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def fixedPoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left, right = 0, len(A) - 1
        while left <= right:
            mid = (left + right) // 2
            if A[mid] == mid:
                return mid
            if A[mid] > mid:
                right = mid - 1
            else:
                left = mid + 1
        return -1
