class Solution(object):
    def countServers(self, grid):
        if not grid:
            return 0
        row_count = [0] * len(grid)
        col_count = [0] * len(grid[0])
        for index_r in range(len(grid)):
            for index_c in range(len(grid[0])):
                if grid[index_r][index_c] == 1:
                    row_count[index_r] += 1
                    col_count[index_c] += 1
        result = 0
        for index_r in range(len(grid)):
            for index_c in range(len(grid[0])):
                if grid[index_r][index_c] == 1 and (row_count[index_r] > 1 or col_count[index_c] > 1):
                    result += 1
        return result
