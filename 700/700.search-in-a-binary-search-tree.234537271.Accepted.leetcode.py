class Solution:
    def searchBST(self, root, val):
        if not root:
            return None
        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


class Solution:
    def searchBST(self, root, val):
        stack = [root]
        while stack:
            root = stack.pop()
            if not root:
                return None
            if root.val == val:
                return root
            elif root.val > val:
                stack.append(root.left)
            else:
                stack.append(root.right)
