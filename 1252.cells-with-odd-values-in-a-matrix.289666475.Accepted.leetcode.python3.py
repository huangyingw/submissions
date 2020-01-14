class Solution(object):
    def oddCells(self, n, m, indices):
        rows = [True] * n
        cols = [True] * m
        for r, c in indices:
            rows[r] = not rows[r]
            cols[c] = not cols[c]
        result = 0
        for r in range(n):
            for c in range(m):
                result += int(rows[r] ^ cols[c])
        return result
