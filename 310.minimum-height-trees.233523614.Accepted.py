from collections import defaultdict


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]
        connections = defaultdict(set)
        for a, b in edges:
            connections[a].add(b)
            connections[b].add(a)
        leaves = set(node for node in connections if len(connections[node]) == 1)
        while len(connections) > 2:
            new_leaves = set()
            for leaf in leaves:
                nbor = connections[leaf].pop()
                connections[nbor].remove(leaf)
                if len(connections[nbor]) == 1:
                    new_leaves.add(nbor)
                del connections[leaf]
            leaves = new_leaves
        return list(connections.keys())
