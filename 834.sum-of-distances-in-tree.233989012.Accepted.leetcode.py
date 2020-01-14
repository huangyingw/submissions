from collections import defaultdict
class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        neighbours = defaultdict(set)
        for a, b in edges:
            neighbours[a].add(b)
            neighbours[b].add(a)
        subtree_counts = [1] * N
        distances = [0] * N
        def subtree_distances(node, parent):
            for child in neighbours[node]:
                if child != parent:
                    subtree_distances(child, node)
                    subtree_counts[node] += subtree_counts[child]
                    distances[node] += distances[child] + subtree_counts[child]
        def update_distances(node, parent):
            for child in neighbours[node]:
                if child != parent:
                    distances[child] = distances[node] - subtree_counts[child] + (N - subtree_counts[child])
                    update_distances(child, node)
        subtree_distances(0, None)
        update_distances(0, None)
        return distances
