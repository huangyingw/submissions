class Solution(object):
    def largestSumOfAverages(self, A, K):
        memo = {}

        def helper(i, k):
            if (i, k) in memo:
                return memo[(i, k)]
            if k == 1:
                memo[(i, k)] = sum(A[:i]) // float(i)
                return memo[(i, k)]
            best = 0
            for j in range(k - 1, i):
                best = max(best, helper(j, k - 1) + sum(A[j:i]) // float(i - j))
            memo[(i, k)] = best
            return best
        return helper(len(A), K)
