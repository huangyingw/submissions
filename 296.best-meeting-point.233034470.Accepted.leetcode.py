class Solution(object):
    def minDistance1D(self, points):
        distance = 0
        i, j = 0, len(points) - 1
        while i < j:
            distance += points[j] - points[i]
            i += 1
            j -= 1
        return distance

    def minTotalDistance(self, grid):
        rows = self.collectRows(grid)
        cols = self.collectCols(grid)
        row = rows[len(rows) / 2]
        col = cols[len(cols) / 2]
        return self.minDistance1D(rows) + self.minDistance1D(cols)

    def collectRows(self, grid):
        rows = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows.append(i)
        return rows

    def collectCols(self, grid):
        cols = []
        for j in range(len(grid[0])):
            for i in range(len(grid)):
                if grid[i][j] == 1:
                    cols.append(j)
        return cols
