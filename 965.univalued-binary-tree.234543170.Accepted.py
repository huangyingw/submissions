









class Solution:
    def isUnivalTree(self, root):

        vals = []

        def dfs(node):
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return len(set(vals)) == 1


class Solution2:
    def isUnivalTree(self, root):
        left_correct = (not root.left or root.val == root.left.val
                        and self.isUnivalTree(root.left))
        right_correct = (not root.right or root.val == root.right.val
                         and self.isUnivalTree(root.right))
        return left_correct and right_correct
