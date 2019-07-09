_author_ = 'jake'
_project_ = 'leetcode'











from copy import deepcopy


class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        house = 0
        distances = deepcopy(grid)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != 1:
                    continue
                q = [(row, col)]
                house_dist = 1
                while q:
                    new_q = []
                    for r, c in q:
                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:

                            if 0 <= r + dr < rows and 0 <= c + dc < cols and grid[r + dr][c + dc] == -house:
                                grid[r + dr][c + dc] -= 1
                                new_q.append((r + dr, c + dc))
                                distances[r + dr][c + dc] += house_dist
                    house_dist += 1
                    q = new_q
                house += 1

        reachable = [distances[r][c] for r in range(rows) for c in range(cols) if grid[r][c] == -house]
        return -1 if not reachable else min(reachable)
