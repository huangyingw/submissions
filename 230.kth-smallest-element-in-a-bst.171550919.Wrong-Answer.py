class Solution(object):
    def kthSmallest(self, root, k):
        if not root:
            return
        self.kthSmallest(root.left, k)
        k -= 1
        if k == 0:
            return root.val
        self.kthSmallest(root.right, k)
