_author_ = 'jake'
_project_ = 'leetcode'
















class Solution(object):
    def checkValidString(self, s):

        min_open, max_open = 0, 0
        for c in s:
            if c == "(":
                min_open += 1
                max_open += 1
            elif c == ")":
                min_open = max(0, min_open - 1)
                max_open -= 1
            else:
                min_open = max(0, min_open - 1)
                max_open += 1
            if max_open < 0:
                return False
        return min_open == 0
