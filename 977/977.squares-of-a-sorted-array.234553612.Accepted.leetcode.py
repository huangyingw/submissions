class Solution(object):
    def sortedSquares(self, A):

        l = len(A)
        j = 0
        while j < l and A[j] < 0:
            j += 1
        i = j - 1
        res = []
        while i >= 0 and j < l:
            if A[i]**2 < A[j]**2:
                res.append(A[i]**2)
                i -= 1
            else:
                res.append(A[j]**2)
                j += 1
        while i >= 0:
            res.append(A[i]**2)
            i -= 1
        while j < l:
            res.append(A[j]**2)
            j += 1
        return res
