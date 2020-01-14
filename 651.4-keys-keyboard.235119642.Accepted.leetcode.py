class Solution(object):
    def maxA(self, N):
        def helper(n):
            if n in memo:
                return memo[n]
            max_A = n
            max_A = max(max_A, helper(i) * (n - i - 1))
            memo[n] = max_A
            return max_A
        memo = {}
        return helper(N)
