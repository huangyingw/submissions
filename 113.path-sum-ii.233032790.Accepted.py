







class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        if root is None:
            return res
        if sum == root.val and root.left is None and root.right is None:
            return [[root.val]]

        left_res = self.pathSum(root.left, sum - root.val)

        right_res = self.pathSum(root.right, sum - root.val)

        for t in left_res + right_res:
            res.append([root.val] + t)
        return res
