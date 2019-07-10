from collections import defaultdict


class Solution(object):
    def gardenNoAdj(self, N, paths):
        edges = defaultdict(set)
        for i, j in paths:
            edges[i].add(j)
            edges[j].add(i)
        flowers = [None] * (N + 1)
        for garden in range(1, N + 1):
            if flowers[garden]:
                continue
            possible_flowers = {1, 2, 3, 4} - {flowers[nbor] for nbor in edges[garden]}
            flowers[garden] = possible_flowers.pop()
        return flowers[1:]
