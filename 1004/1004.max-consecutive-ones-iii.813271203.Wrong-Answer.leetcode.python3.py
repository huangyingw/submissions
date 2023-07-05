class Solution(object):
    def longestOnes(self, A, K):
        i = 0
        for j in range(len(A)):
            if A[j] == 0:
                K -= 1
            while K < 0 and i < j:
                if A[i] == 0:
                    K += 1
                i += 1
        return j - i + 1
