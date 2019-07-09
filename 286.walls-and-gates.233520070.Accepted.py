_author_ = 'jake'
_project_ = 'leetcode'











from collections import deque


class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return
        INF = 2 ** 31 - 1
        rows, cols = len(rooms), len(rooms[0])
        frontier = deque([(r, c) for r in range(rows) for c in range(cols) if rooms[r][c] == 0])
        while frontier:
            row, col = frontier.popleft()
            for i, j in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                if i >= 0 and i < rows and j >= 0 and j < cols:
                    if rooms[i][j] == INF:
                        rooms[i][j] = rooms[row][col] + 1
                        frontier.append((i, j))
