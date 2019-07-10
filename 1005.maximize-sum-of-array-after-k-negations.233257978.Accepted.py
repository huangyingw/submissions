_author_ = 'jake'
_project_ = 'leetcode'












class Solution(object):
    def largestSumAfterKNegations(self, A, K):

        A.sort()
        i = 0
        while K > 0 > A[i]:
            A[i] = -A[i]
            i += 1
            K -= 1
        result = sum(A)
        if K % 2 == 1:
            result -= 2 * min(A[i], float("inf") if i == 0 else A[i - 1])
        return result
