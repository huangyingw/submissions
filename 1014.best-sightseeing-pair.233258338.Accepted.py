_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def maxScoreSightseeingPair(self, A):

        best_minus_dist = 0
        result = 0
        for num in A:
            result = max(result, num + best_minus_dist)
            best_minus_dist = max(best_minus_dist - 1, num - 1)
        return result
