_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for s in S:
            if s == "(":
                stack.append(s)
            else:
                item = stack.pop()
                if item == "(":
                    num = 1
                else:
                    stack.pop()
                    num = 2 * item
                if stack and stack[-1] != "(":
                    stack[-1] += num
                else:
                    stack.append(num)
        return stack[0]
