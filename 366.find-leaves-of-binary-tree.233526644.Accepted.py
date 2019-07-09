_author_ = 'jake'
_project_ = 'leetcode'














class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
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
