from collections import defaultdict
class Solution(object):
    def minFlips(self, mat):
        rows, cols = len(mat), len(mat[0])
        linear = []
        for row in mat:
            linear += [bool(cell) for cell in row]
        linear_nbors = defaultdict(list)
        for r in range(rows):
            for c in range(cols):
                i = r * cols + c
                linear_nbors[i].append(i)
                for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    if 0 <= r + dr < rows and 0 <= c + dc < cols:
                        j = (r + dr) * cols + (c + dc)
                        linear_nbors[i].append(j)
        frontier = {tuple(linear)}
        steps = 0
        seen = set()
        while frontier:
            new_frontier = set()
            for state in frontier:
                if all(not v for v in state):
                    return steps
                if state in seen:
                    continue
                seen.add(state)
                for i in range(rows * cols):
                    new_state = list(state)
                    for nbor in linear_nbors[i]:
                        new_state[nbor] = not (new_state[nbor])
                    new_frontier.add((tuple(new_state)))
            steps += 1
            frontier = new_frontier
        return -1
