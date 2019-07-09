_author_ = 'jake'
_project_ = 'leetcode'










class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = 1
        for even in range(0, len(A), 2):
            if A[even] % 2 == 1:
                while A[odd] % 2 == 1:
                    odd += 2
                A[odd], A[even] = A[even], A[odd]
        return A
