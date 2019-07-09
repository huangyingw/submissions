








class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        self.result = 0
        cache = {0: 1}

        self.dfs(root, sum, 0, cache)

        return self.result

    def dfs(self, root, target, currPathSum, cache):

        if root is None:
            return

        currPathSum += root.val
        oldPathSum = currPathSum - target

        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1

        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)

        cache[currPathSum] -= 1
