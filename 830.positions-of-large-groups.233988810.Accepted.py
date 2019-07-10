_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def largeGroupPositions(self, S):

        result = []
        start = 0
        for i, c in enumerate(S):
            if i == len(S) - 1 or c != S[i + 1]:
                if i - start >= 2:
                    result.append([start, i])
                start = i + 1
        return result
