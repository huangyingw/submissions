class Solution:
    def pathSum(self, root, sum):
        if not root:
            return []
        res = []
        stack = [(root, sum - root.val, [root.val])]
        while stack:
            curr, val, ls = stack.pop()
            if not curr.left and not curr.right and val == curr.val:
                res.append(ls + [curr.val])
            if root.left:
                stack.append((root.left, val - curr.val, ls + [curr.val]))
            if root.right:
                stack.append((root.right, val - curr.val, ls + [curr.val]))
        return res
