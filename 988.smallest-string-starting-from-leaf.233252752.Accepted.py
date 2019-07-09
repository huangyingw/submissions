# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        self.result = "~"

        def dfs(node, A):
            if node:
                A.append(chr(node.val + ord('a')))
                if not node.left and not node.right:
                    self.result = min(self.result, "".join(reversed(A)))
                dfs(node.left, A)
                dfs(node.right, A)
                A.pop()
        dfs(root, [])
        return self.result
