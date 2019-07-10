_author_ = 'jake'
_project_ = 'leetcode'

















class Solution(object):
    def removeOuterParentheses(self, S):

        result = []
        balance = 0
        for c in S:
            if balance != 0:
                result.append(c)
            change = 1 if c == "(" else -1
            balance += change
            if balance == 0:
                result.pop()
        return "".join(result)
