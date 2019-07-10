_author_ = 'jake'
_project_ = 'leetcode'












class Solution(object):
    def hasPath(self, maze, start, destination):

        queue = [start]
        dirns = ((1, 0), (-1, 0), (0, 1), (0, -1))
        visited = set()
        while queue:
            start_r, start_c = queue.pop()
            visited.add((start_r, start_c))
            for dr, dc in dirns:
                r, c = start_r, start_c
                while 0 <= r + dr < len(maze) and 0 <= c + dc < len(maze[0]) and maze[r + dr][c + dc] == 0:
                    r += dr
                    c += dc
                if (r, c) not in visited:
                    if [r, c] == destination:
                        return True
                    queue.append((r, c))
        return False
