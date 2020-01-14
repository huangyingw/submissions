from collections import defaultdict
class Solution(object):
    def deleteTreeNodes(self, nodes, parents, values):
        node_children = defaultdict(list)
        for child, parent in enumerate(parents):
            node_children[parent].append(child)
        def helper(node):
            subtree_sum = values[node]
            subtree_count = 1
            for child in node_children[node]:
                child_sum, child_count = helper(child)
                subtree_sum += child_sum
                subtree_count += child_count
            if subtree_sum == 0:
                subtree_count = 0
            return (subtree_sum, subtree_count)
        _, result = helper(0)
        return result
