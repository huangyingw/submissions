from collections import defaultdict


class Solution(object):
    def criticalConnections(self, n, connections):
        node_to_nbors = defaultdict(list)
        for connection in connections:
            node_to_nbors[connection[0]].append(connection[1])
            node_to_nbors[connection[1]].append(connection[0])
        connections = {tuple(sorted(connection)) for connection in connections}
        rank = [-float("inf")] * n

        def helper(node, depth):
            if rank[node] >= 0:
                return rank[node]
            rank[node] = depth
            min_nbor_path_depth = n
            for nbor in node_to_nbors[node]:
                if rank[nbor] == depth - 1:
                    continue
                nbor_path_depth = helper(nbor, depth + 1)
                if nbor_path_depth <= depth:
                    connections.discard(tuple(sorted((node, nbor))))
                min_nbor_path_depth = min(min_nbor_path_depth, nbor_path_depth)
            rank[node] = n
            return min_nbor_path_depth
        helper(0, 0)
        return list(connections)
