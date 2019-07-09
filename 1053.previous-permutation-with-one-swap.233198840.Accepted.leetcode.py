class Solution(object):
    def prevPermOpt1(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        left, right = len(A) - 2, len(A) - 1
        for left in range(len(A) - 2, -1, -1):
            if A[left] > A[left + 1]:
                break
        else:
            return A
        right = A.index(max(ele for ele in A[left + 1:] if ele < A[left]), left)
        A[left], A[right] = A[right], A[left]
        return A
