from collections import defaultdict
class Solution(object):
    def treeDiameter(self, edges):
        node_to_nbors = defaultdict(set)
        for a, b in edges:
            node_to_nbors[a].add(b)
            node_to_nbors[b].add(a)
        leaves = {node for node, nbors in node_to_nbors.items() if len(nbors) == 1}
        result = 0
        while len(leaves) > 1:
            new_leaves = set()
            for leaf in leaves:
                nbor = node_to_nbors[leaf].pop()
                if nbor in leaves:
                    result += 1
                    break
                node_to_nbors[nbor].remove(leaf)
                if len(node_to_nbors[nbor]) == 1:
                    new_leaves.add(nbor)
            else:
                result += 2
            leaves = new_leaves
        return result
