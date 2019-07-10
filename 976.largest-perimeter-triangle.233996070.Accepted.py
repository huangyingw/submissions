_author_ = 'jake'
_project_ = 'leetcode'











class Solution:
    def largestPerimeter(self, A):

        A.sort(reverse=True)
        for i, side in enumerate(A[:-2]):
            if side < A[i + 1] + A[i + 2]:
                return side + A[i + 1] + A[i + 2]
        return 0
