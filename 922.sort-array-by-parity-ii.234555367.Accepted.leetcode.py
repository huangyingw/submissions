class Solution(object):
    def sortArrayByParityII(self, A):
        index = 0
        for i in range(1, len(A), 2):
            if A[i] % 2 == 0 and index < len(A):
                while A[index] % 2 == 0:
                    index += 2
                A[index], A[i] = A[i], A[index]
                index += 2
        return A
