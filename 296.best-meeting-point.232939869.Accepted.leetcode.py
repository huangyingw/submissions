class Solution(object):
    def minTotalDistance(self, grid):
        rowGrid = grid
        colGrid = zip(*grid)
        total = 0
        for grid in rowGrid, colGrid:
            tempGrid = []
            for position, point in enumerate(grid):
                tempGrid += [position] * sum(point)
            for p in tempGrid:
                total += abs(p - tempGrid[len(tempGrid) / 2])
        return total
