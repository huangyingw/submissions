class Solution(object):
    def numEnclaves(self, A):
        rows, cols = len(A), len(A[0])
        result = 0
        self.edge = False
        def enclave(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return 0
            if A[r][c] != 1:
                return 0
            if r == 0 or c == 0 or r == rows - 1 or c == cols - 1:
                self.edge = True
            A[r][c] = 0
            count = 1
            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                count += enclave(r + dr, c + dc)
            return count if not self.edge else 0
        for r in range(rows):
            for c in range(cols):
                self.edge = False
                result += enclave(r, c)
        return result
