class Solution(object):
    def addToArrayForm(self, A, K):
        for i in range(len(A) - 1, -1, -1):
            A[i] += K
            K, A[i] = divmod(A[i], 10)
        return [int(c) for c in str(K)] + A if K else A
