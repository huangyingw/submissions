_author_ = 'jake'
_project_ = 'leetcode'








class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        valid = []
        self.remove(s, valid, 0, 0, ('(', ')'))
        return valid

    def remove(self, s, valid, start, removed, par):
        net_open = 0
        for i in range(start, len(s)):
            net_open += ((s[i] == par[0]) - (s[i] == par[1]))
            if net_open >= 0:
                continue

            for j in range(removed, i + 1):
                if s[j] == par[1] and (j == removed or s[j - 1] != par[1]):
                    self.remove(s[:j] + s[j + 1:], valid, i, j, par)
            return
        reversed = s[::-1]
        if par[0] == '(':
            self.remove(reversed, valid, 0, 0, (')', '('))
        else:
            valid.append(reversed)
