_author_ = 'jake'
_project_ = 'leetcode'













from collections import deque


class Solution(object):
    def findShortestWay(self, maze, ball, hole):
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int]
        :rtype: str
        """
        def maze_cell(r, c):
            if [r, c] == hole:
                return -1
            elif 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] == 0:
                return 0
            return 1

        def vertical(dirn):
            return dirn in {"d", "u"}

        def perpendicular(dirn):
            return ["r", "l"] if vertical(dirn) else ["u", "d"]
        visited = set()
        queue = deque()
        dirns = {"d": (1, 0), "u": (-1, 0), "r": (0, 1), "l": (0, -1)}
        for dirn in "dlru":
            queue.append((ball[0], ball[1], [dirn]))
        while queue:
            r, c, moves = queue.popleft()
            if (r, c, moves[-1]) in visited:
                continue
            visited.add((r, c, moves[-1]))
            dr, dc = dirns[moves[-1]]
            nm = maze_cell(r + dr, c + dc)
            if nm == -1:
                return "".join(moves)

            elif nm == 0:
                queue.append((r + dr, c + dc, moves))

            elif [r, c] != ball:
                trial_dirns = perpendicular(moves[-1])
                for trial_dirn in trial_dirns:
                    queue.appendleft((r, c, moves + [trial_dirn]))
        return "impossible"
