













class Solution(object):
    def findLeaves(self, root):

        leaves = []
        self.height(root, leaves)
        return leaves

    def height(self, node, leaves):
        if not node:
            return -1
        h = 1 + max(self.height(node.left, leaves), self.height(node.right, leaves))
        if h >= len(leaves):
            leaves.append([])
        leaves[h].append(node.val)
        return h
