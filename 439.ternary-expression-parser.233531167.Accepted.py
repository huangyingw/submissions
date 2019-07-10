_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def parseTernary(self, expression):

        stack = []
        for c in expression[::-1]:
            if stack and stack[-1] == "?":
                stack.pop()
                true_val = stack.pop()
                stack.pop()
                false_val = stack.pop()
                if c == "T":
                    stack.append(true_val)
                else:
                    stack.append(false_val)
            else:
                stack.append(c)
        return stack.pop()
