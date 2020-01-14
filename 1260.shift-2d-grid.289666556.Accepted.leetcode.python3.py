class Solution(object):
    def shiftGrid(self, grid, k):
        rows, cols = len(grid), len(grid[0])
        n = rows * cols
        result = [[]]
        for i in range(n):
            if len(result[-1]) == cols:
                result.append([])
            prev = (i - k) % n
            r, c = divmod(prev, cols)
            result[-1].append(grid[r][c])
        return result
