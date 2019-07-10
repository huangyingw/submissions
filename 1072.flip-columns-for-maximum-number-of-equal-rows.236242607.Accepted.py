_author_ = 'jake'
_project_ = 'leetcode'












from collections import defaultdict


class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):

        row_counter = defaultdict(int)
        for row in matrix:
            row_counter[tuple(x ^ row[0] for x in row)] += 1
        return max(row_counter.values())
