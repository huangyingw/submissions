


class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        index = 0
        while K > 0:
            if A[index] < 0:
                A[index] *= -1
                if A[index + 1] < A[index] and index < len(A) - 1:
                    index += 1
            else:
                A[index] *= -1
            K -= 1
        return sum(A)
