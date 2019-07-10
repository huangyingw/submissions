class Solution(object):
    def maxScoreSightseeingPair(self, A):

        prev_best, result = 0, 0
        for index in range(0, len(A)):
            result = max(result, A[index] - index + prev_best)
            prev_best = max(prev_best, A[index] + index)
        return result
