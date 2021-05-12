class Solution(object):
    def clumsy(self, N):
        return [0, 1, 2, 6, 7][N] if N < 5 else N + [1, 2, 2, - 1][N % 4]
