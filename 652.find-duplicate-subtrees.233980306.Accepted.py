from collections import defaultdict


class Solution(object):
    def findDuplicateSubtrees(self, root):
        def serialize(node):
            if not node:
                return "
            serial = str(node.val) + "," + serialize(node.left) + "," + serialize(node.right)
            subtrees[serial].append(node)
            return serial
        subtrees = defaultdict(list)
        serialize(root)
        return [nodes[0] for serial, nodes in subtrees.items() if len(nodes) > 1]
