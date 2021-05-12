class Solution(object):
    def minDominoRotations(self, A, B):
        n = len(A)
        for num in range(1, 7):
            if all(a == num or b == num for a, b in zip(A, B)):
                return min(n - A.count(num), n - B.count(num))
        return -1
