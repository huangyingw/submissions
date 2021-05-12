class Solution(object):
    def shortestDistanceColor(self, colors, queries):
        shortest = []
        distances = [float("inf")] * 3
        for color in colors:
            distances = [d + 1 for d in distances]
            distances[color - 1] = 0
            shortest.append(list(distances))
        for i in range(len(colors) - 2, -1, -1):
            distances = [d + 1 for d in shortest[i + 1]]
            for color in range(3):
                shortest[i][color] = min(shortest[i][color], distances[color])
        result = []
        for i, color in queries:
            shortest_dist = shortest[i][color - 1]
            result.append(-1 if shortest_dist == float("inf") else shortest_dist)
        return result
