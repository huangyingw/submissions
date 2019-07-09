_author_ = 'jake'
_project_ = 'leetcode'














class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        def helper(n):
            if n in memo:
                return memo[n]
            max_A = n
            for i in range(max(n - 5, 0), n - 3):
                max_A = max(max_A, helper(i) * (n - i - 1))
            memo[n] = max_A
            return max_A
        memo = {}
        return helper(N)
