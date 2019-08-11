class Solution(object):
    def kthSmallest(self, root, k):
        if not root or k < 0:
            return
        self.kthSmallest(root.left, k - 1)
        if k == 0:
            return root.val
        self.kthSmallest(root.right, k - 1)
