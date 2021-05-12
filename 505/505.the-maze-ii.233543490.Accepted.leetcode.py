class Solution(object):
    def shortestDistance(self, maze, start, destination):
        rows, cols = len(maze), len(maze[0])
        distance = 0
        visited = set()
        dirns = {"u": (-1, 0), "d": (1, 0), "l": (0, -1), "r": (0, 1)}
        perps = {"u": ("l", "r"), "d": ("l", "r"), "l": ("u", "d"), "r": ("u", "d")}
        queue = [(start[0], start[1], d) for d in dirns]
        while queue:
            new_queue = []
            while queue:
                r, c, dirn = queue.pop()
                if ((r, c, dirn)) in visited:
                    continue
                visited.add((r, c, dirn))
                dr, dc = dirns[dirn]
                if 0 <= r + dr < rows and 0 <= c + dc < cols and maze[r + dr][c + dc] == 0:
                    new_queue.append((r + dr, c + dc, dirn))
                else:
                    if [r, c] == destination:
                        return distance
                    perp = perps[dirn]
                    for new_dirn in perp:
                        queue.append((r, c, new_dirn))
            distance += 1
            queue = new_queue
        return -1
