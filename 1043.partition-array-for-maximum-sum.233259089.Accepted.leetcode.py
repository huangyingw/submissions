









class Solution(object):
    def maxSumAfterPartitioning(self, A, K):

        results = [0]
        for i in range(len(A)):
            subarray_max, max_result = 0, 0
            for j in range(i, max(-1, i - K), -1):
                subarray_max = max(subarray_max, A[j])
                max_result = max(max_result, subarray_max * (i - j + 1) + results[j])
            results.append(max_result)
        return results[-1]
