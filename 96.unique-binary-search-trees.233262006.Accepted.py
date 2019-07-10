








class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def numTrees(self, n):

        memo = [-1] * (n + 1)
        return self.helper(n, memo)

    def helper(self, n, memo):
        if n <= 1:
            return 1
        if memo[n] != -1:
            return memo[n]
        count = 0
        for i in range(1, n + 1):


            count += self.helper(i - 1, memo) * self.helper(n - i, memo)
        memo[n] = count
        return count
