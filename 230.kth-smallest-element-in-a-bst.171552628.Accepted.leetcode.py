class Solution(object):
    def kthSmallest(self, root, k):
        result = []
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                k -= 1
                if k == 0:
                    return root.val
                root = root.right
        return result
