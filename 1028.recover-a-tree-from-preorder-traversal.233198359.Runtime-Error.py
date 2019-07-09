


class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        from collections import defaultdict
        dp = defaultdict(int)
        # print dp
        for index_i in range(len(A)):
            for index_j in range(index_i):
                diff = A[index_i] - A[index_j]
                dp[(index_i, diff)] = max(dp[(index_i, diff)], dp[(index_j, diff)] + 1)
                # print dp
        return max(dp.itervalues()) + 1
