from collections import defaultdict


class Solution(object):
    def leadsToDestination(self, n, edges, source, destination):
        visited = set()
        edge_dict = defaultdict(set)
        for start, end in edges:
            edge_dict[start].add(end)

        def can_reach_dest(node):
            if node == destination and len(edge_dict[node]) == 0:
                return True
            if node == destination or len(edge_dict[node]) == 0:
                return False
            if node in visited:
                return False
            visited.add(node)
            result = all(can_reach_dest(nbor) for nbor in edge_dict[node])
            visited.remove(node)
            return result
        return can_reach_dest(source)
