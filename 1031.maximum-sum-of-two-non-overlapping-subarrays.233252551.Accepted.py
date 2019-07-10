class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):

        cumm_sum = [0]
        for index in range(len(A)):
            cumm_sum.append(cumm_sum[index] + A[index])
        result = 0

        def valid(index_i, index_j):
            return index_i + L <= len(A) and index_j + M <= len(A) and(index_j >= index_i + L or index_i >= index_j + M)
        for index_i in range(len(A)):
            for index_j in range(len(A)):
                if valid(index_i, index_j):
                    result = max(result, cumm_sum[index_i + L] - cumm_sum[index_i] + cumm_sum[index_j + M] - cumm_sum[index_j])
        return result
