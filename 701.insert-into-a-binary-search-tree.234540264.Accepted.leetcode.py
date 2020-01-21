class Solution:
    def insertIntoBST(self, root, val):
        def helper(node, val):
            if node:
                if node.val < val and not node.right:
                    node.right = TreeNode(val)
                    return
                elif node.val > val and not node.left:
                    node.left = TreeNode(val)
                    return
                if node.val < val:
                    helper(node.right, val)
                else:
                    helper(node.left, val)
        helper(root, val)
        return root
