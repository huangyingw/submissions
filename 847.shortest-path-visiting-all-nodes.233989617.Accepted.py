_author_ = 'jake'
_project_ = 'leetcode'












class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        if len(graph) == 0 or len(graph[0]) == 0:
            return 0
        n = len(graph)
        frontier = {(1 << node, node) for node in range(n)}
        visited = set(frontier)
        distance = 0
        while True:
            new_frontier = set()
            for bit_nodes, node in frontier:
                if bit_nodes == 2 ** n - 1:
                    return distance
                for nbor in graph[node]:
                    new_bit_nodes = bit_nodes | 1 << nbor
                    if (new_bit_nodes, nbor) not in visited:
                        new_frontier.add((new_bit_nodes, nbor))
            visited |= new_frontier
            distance += 1
            frontier = new_frontier
