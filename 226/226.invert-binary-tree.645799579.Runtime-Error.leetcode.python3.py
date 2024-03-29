class Solution:
    def invertTree(self, root: TreeNode):
        if not root:
            return []
        queue = []
        queue.append(root)
        while queue:
            cur = queue.pop(0)
            cur.left, cur.right = cur.right, cur.left
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return root
