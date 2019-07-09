_author_ = 'jake'
_project_ = 'leetcode'















class Solution(object):
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        def splitter(node):
            if not node:
                return [None, None]
            if V < node.val:
                less, more = splitter(node.left)
                node.left = more
                return [less, node]
            less, more = splitter(node.right)
            node.right = less
            return [node, more]
        return splitter(root)
