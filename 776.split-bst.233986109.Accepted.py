














class Solution(object):
    def splitBST(self, root, V):

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
