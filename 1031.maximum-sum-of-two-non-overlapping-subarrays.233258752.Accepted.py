_author_ = 'jake'
_project_ = 'leetcode'


















class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):

        L_sum, M_sum = sum(A[M:L + M]), sum(A[L:L + M])
        L_before_M_sum, M_before_L_sum = sum(A[:L]), sum(A[:M])
        L_before_M_best, M_before_L_best = L_before_M_sum, M_before_L_sum
        result = sum(A[:L + M])
        for i in range(L + M, len(A)):
            L_sum = L_sum + A[i] - A[i - L]
            M_before_L_sum = M_before_L_sum + A[i - L] - A[i - L - M]
            M_before_L_best = max(M_before_L_best, M_before_L_sum)
            result = max(result, L_sum + M_before_L_best)
            M_sum = M_sum + A[i] - A[i - M]
            L_before_M_sum = L_before_M_sum + A[i - M] - A[i - M - L]
            L_before_M_best = max(L_before_M_best, L_before_M_sum)
            result = max(result, M_sum + L_before_M_best)
        return result
