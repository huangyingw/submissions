_author_ = 'jake'
_project_ = 'leetcode'
















class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root or not root.left:
            return root
        new_root = self.upsideDownBinaryTree(root.left)
        node = new_root
        while node.right:
            node = node.right
        node.left = root.right
        node.right = root
        root.left = None
        root.right = None
        return new_root
