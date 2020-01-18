class Solution(object):
    def sortArrayByParityII(self, A):
        odd = 1
        for i in xrange(0, len(A), 2):
            if A[i] % 2:
                while A[odd] % 2:
                    odd += 2
                A[i], A[odd] = A[odd], A[i]
        return A
