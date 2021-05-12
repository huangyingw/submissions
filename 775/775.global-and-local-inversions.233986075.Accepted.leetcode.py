class Solution(object):
    def isIdealPermutation(self, A):
        max_before_prev = -1
        for i in range(1, len(A)):
            if A[i] < max_before_prev:
                return False
            max_before_prev = max(max_before_prev, A[i - 1])
        return True
