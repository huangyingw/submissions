







class Solution(object):





    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        node, parent, parentRight = root, None, None
        while node is not None:
            left = node.left
            node.left = parentRight
            parentRight = node.right
            node.right = parent
            parent = node
            node = left
        return parent
