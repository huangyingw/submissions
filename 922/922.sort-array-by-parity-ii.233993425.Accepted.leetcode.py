class Solution:
    def sortArrayByParityII(self, A):
        odd = 1
        for even in range(0, len(A), 2):
            if A[even] % 2 == 1:
                while A[odd] % 2 == 1:
                    odd += 2
                A[odd], A[even] = A[even], A[odd]
        return A
