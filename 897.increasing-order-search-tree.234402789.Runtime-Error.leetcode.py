class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution1:
    def increasingBST(self, root):
        def inorder(node, ans):
            if not node:
                return
            inorder(node.left, ans)
            ans.append(node.val)
            inorder(node.right, ans)
        vals = []
        inorder(root, vals)
        cur = res = TreeNode(0)
        for v in vals:
            cur.right = TreeNode(v)
            cur = cur.right
        return res.right
class Solution2:
    def increasingBST(self, root, tail=None):
        if not root:
            return tail
        res = self.increasingBST(root.left, root)
        root.left = None
        root.right = self.increasingBST(root.right, tail)
        return res
