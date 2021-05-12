class Solution(object):
    def canWin(self, s):
        def helper(s):
            if s in memo:
                return memo[s]
            for i in range(len(s) - 1):
                if s[i:i + 2] == '++' and not helper(s[:i] + '--' + s[i + 2:]):
                    memo[s] = True
                    return True
            memo[s] = False
            return False
        memo = {}
        return helper(s)
