_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def minTotalDistance(self, grid):

        rows, cols = [], []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    rows.append(r)
                    cols.append(c)
        cols.sort()
        dist = 0
        left, right = 0, len(rows) - 1
        while left < right:
            dist += (rows[right] - rows[left])
            left += 1
            right -= 1
        left, right = 0, len(cols) - 1
        while left < right:
            dist += (cols[right] - cols[left])
            left += 1
            right -= 1
        return dist
