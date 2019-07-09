_author_ = 'jake'
_project_ = 'leetcode'
















class Solution:
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        unvisited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    start = (r, c)
                elif grid[r][c] == 2:
                    end = (r, c)
                    unvisited.add((r, c))
                elif grid[r][c] == 0:
                    unvisited.add((r, c))

        def make_paths(r, c):
            if not unvisited and (r, c) == end:
                return 1
            if not unvisited or (r, c) == end:
                return 0
            paths = 0
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nbor_r, nbor_c = r + dr, c + dc
                if (nbor_r, nbor_c) in unvisited:
                    unvisited.remove((nbor_r, nbor_c))
                    paths += make_paths(nbor_r, nbor_c)
                    unvisited.add((nbor_r, nbor_c))
            return paths
        return make_paths(*start)
