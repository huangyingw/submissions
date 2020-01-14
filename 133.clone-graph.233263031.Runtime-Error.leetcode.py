class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []
class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return
        cloned_start = UndirectedGraphNode(node.label)
        to_clone = [node]
        node_mapping = {node: cloned_start}
        while to_clone:
            node = to_clone.pop()
            clone_node = node_mapping[node]
            for neighbor in node.neighbors:
                if neighbor not in node_mapping:
                    clone_neightbor = UndirectedGraphNode(neighbor.label)
                    node_mapping[neighbor] = clone_neightbor
                    to_clone.append(neighbor)
                else:
                    clone_neightbor = node_mapping[neighbor]
                clone_node.neighbors.append(clone_neightbor)
        return cloned_start
