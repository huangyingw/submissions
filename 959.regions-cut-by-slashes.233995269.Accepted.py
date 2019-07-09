_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        n = len(grid)
        UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
        parents = {}

        def find(node):
            parents.setdefault(node, node)
            while parents[node] != node:
                parents[node] = parents[parents[node]]
                node = parents[node]
            return node

        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            parents[parent2] = parent1
        for r in range(n):
            for c in range(n):
                if r != n - 1:
                    union((r, c, DOWN), (r + 1, c, UP))
                if c != n - 1:
                    union((r, c, RIGHT), (r, c + 1, LEFT))
                if grid[r][c] == "/":
                    union((r, c, UP), (r, c, LEFT))
                    union((r, c, DOWN), (r, c, RIGHT))
                elif grid[r][c] == "\\":
                    union((r, c, UP), (r, c, RIGHT))
                    union((r, c, DOWN), (r, c, LEFT))
                else:
                    union((r, c, UP), (r, c, LEFT))
                    union((r, c, UP), (r, c, DOWN))
                    union((r, c, UP), (r, c, RIGHT))
        return len({find(node) for node in parents.keys()})
