class Solution(object):
    def pathSum(self, root, sum):
        res = []
        if root is None:
            return res
        if sum == root.val and root.left is None and root.right is None:
            return [[root.val]]

        left_res = self.pathSum(root.left, sum - root.val)

        right_res = self.pathSum(root.right, sum - root.val)

        return res
