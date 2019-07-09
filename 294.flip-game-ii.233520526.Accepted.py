_author_ = 'jake'
_project_ = 'leetcode'












class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
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
