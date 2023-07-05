class Solution(object):
    def longestOnes(self, A, K):
        i = 0
        for j in range(len(A)):
            if A[j] == 0:
                K -= 1
            if K < 0:
                if A[i] == 0:
                    K += 1
                i += 1
        return j - i + 1
