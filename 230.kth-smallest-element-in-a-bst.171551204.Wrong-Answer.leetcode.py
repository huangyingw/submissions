class Solution(object):
    def kthSmallest(self, root, k):
        if not root:
            return
        ret = self.kthSmallest(root.left, k)
        k -= 1
        if k == 0:
            return ret
        ret = self.kthSmallest(root.right, k)
