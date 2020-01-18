class Solution(object):
    def generateParenthesis(self, n):
        result = []

        def backtracking(S, left, right):
            if len(S) == 2 * n:
                result.append(S)
