_author_ = 'jake'
_project_ = 'leetcode'

















class Solution(object):
    def containVirus(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        used_walls = 0

        def get_nbors(r, c):
            if (r, c) in visited:
                return
            visited.add((r, c))
            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                r1, c1 = r + dr, c + dc
                if r1 < 0 or r1 >= rows or c1 < 0 or c1 >= cols:
                    continue
                if grid[r1][c1] == 2:
                    continue
                if grid[r1][c1] == 0:
                    nbors.add((r1, c1))
                    walls[0] += 1
                else:
                    get_nbors(r1, c1)

        def contain_region(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] != 1:
                return
            grid[r][c] = 2
            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                contain_region(r + dr, c + dc)
        while True:
            regions = []
            visited = set()
            for r in range(rows):
                for c in range(cols):

                    if (r, c) not in visited and grid[r][c] == 1:
                        nbors, walls = set(), [0]
                        get_nbors(r, c)
                        regions.append([(r, c), set(nbors), walls[0]])
            regions.sort(key=lambda x: -len(x[1]))
            if not regions or len(regions[0][1]) == 0:
                return used_walls
            used_walls += regions[0][2]
            contain_region(regions[0][0][0], regions[0][0][1])
            for _, expansion, _ in regions[1:]:
                for r, c in expansion:
                    grid[r][c] = 1
