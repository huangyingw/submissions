_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n < 3:
            return 0
        diff = A[1] - A[0]
        start, slices = 0, 0
        for i in range(2, n):
            next_diff = A[i] - A[i - 1]
            if next_diff == diff:
                slices += i - start - 1
            else:
                diff = next_diff
                start = i - 1
        return slices
