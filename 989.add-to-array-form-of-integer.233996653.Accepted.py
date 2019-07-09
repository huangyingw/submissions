_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        for i in range(len(A) - 1, -1, -1):
            A[i] += K
            K, A[i] = divmod(A[i], 10)
        return [int(c) for c in str(K)] + A if K else A
