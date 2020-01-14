class Solution:
    def cloneGraph(self, node):
        mapping = dict()
        def clone(root):
            if not root:
                return None
            if root.label in mapping:
                return mapping[root.label]
            new_root = UndirectedGraphNode(root.label)
            mapping[root.label] = new_root
            for n in root.neighbors:
                new_root.neighbors.append(clone(n))
            return new_root
        return clone(node)
