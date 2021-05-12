class Solution(object):
    def generateMatrix(self, n):
        spiral = [[0 for _ in range(n)] for _ in range(n)]
        row, col = 0, 0
        d_r, d_c = 0, 1
        count = 1
        while count <= n * n:
            spiral[row][col] = count
            count += 1
            if row + d_r < 0 or row + d_r >= n or col + d_c < 0 or col + d_c >= n or spiral[row + d_r][col + d_c] != 0:
                d_r, d_c = d_c, -d_r
            row += d_r
            col += d_c
        return spiral
