









class Solution(object):
    def numMagicSquaresInside(self, grid):

        def is_magic(row, col):
            if grid[row + 1][col + 1] != 5:
                return False
            line_sums = [0 for _ in range(6)]
            diag1, diag2 = 0, 0
            for dr in range(3):
                for dc in range(3):
                    val = grid[row + dr][col + dc]
                    if val < 1 or val > 9:
                        return False
                    line_sums[dr] += val
                    line_sums[dc + 3] += val
                    if dr == dc:
                        diag1 += val
                    if dr + dc == 2:
                        diag2 += val
            if any(line_sum != 15 for line_sum in line_sums):
                return False
            if diag1 != 15 or diag2 != 15:
                return False
            return True
        rows, cols = len(grid), len(grid[0])
        magic = 0
        for r in range(rows - 2):
            for c in range(cols - 2):
                magic += is_magic(r, c)
        return magic
