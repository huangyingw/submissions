from collections import defaultdict


class Solution(object):
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        red, blue = defaultdict(list), defaultdict(list)
        for start, end in red_edges:
            red[start].append(end)
        for start, end in blue_edges:
            blue[start].append(end)
        result = [-1] * n
        frontier = [(0, True), (0, False)]
        steps = 0
        visited = set()
        while frontier:
            new_frontier = []
            for node, is_red in frontier:
                if (node, is_red) in visited:
                    continue
                visited.add((node, is_red))
                if result[node] == -1:
                    result[node] = steps
                nbors = red[node] if is_red else blue[node]
                new_frontier += [(nbor, not is_red) for nbor in nbors]
            frontier = new_frontier
            steps += 1
        return result
