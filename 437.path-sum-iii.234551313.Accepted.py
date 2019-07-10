








class Solution(object):
    def pathSum(self, root, sum):

        self.result = 0
        self.helper(root, sum, 0, {0: 1})
        return self.result

    def helper(self, root, target, currPathSum, cache):
        if not root:
            return
        complement = currPathSum + root.val - target
        if complement in cache:
            self.result += cache[complement]
        cache.setdefault(currPathSum + root.val, 0)
        cache[currPathSum + root.val] += 1
        self.helper(root.left, target, currPathSum + root.val, cache)
        self.helper(root.right, target, currPathSum + root.val, cache)
        cache[currPathSum + root.val] -= 1
