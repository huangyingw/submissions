class Solution(object):
    def twoSumLessThanK(self, A, K):
        result = -1
        A.sort()
        left, right = 0, len(A) - 1
        while left < right:
            if A[left] + A[right] < K:
                result = max(result, A[left] + A[right])
                left += 1
            else:
                right -= 1
        return result
