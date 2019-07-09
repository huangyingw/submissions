








class Solution(object):

















    def pathSumHelper(self, root, target, so_far, cache):
        if root:

            complement = so_far + root.val - target
            if complement in cache:

                self.result += cache[complement]
            cache[so_far + root.val] = cache.get(so_far + root.val, 0) + 1
            self.pathSumHelper(root.left, target, so_far + root.val, cache)
            self.pathSumHelper(root.right, target, so_far + root.val, cache)
            cache[so_far + root.val] -= 1
        return

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.result = 0
        self.pathSumHelper(root, sum, 0, {0: 1})
        return self.result
