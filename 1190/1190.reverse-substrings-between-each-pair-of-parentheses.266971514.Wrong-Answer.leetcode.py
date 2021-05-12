class Solution(object):
    def reverseParentheses(self, s):
        stack = [""]
        start = 0
        for i, c in enumerate(s):
            if c == "(":
                stack[-1] += s[start:i]
                stack.append("")
                start = i + 1
            elif c == ")":
                stack[-1] += s[start:i]
                stack[-1] += stack.pop()[::-1]
                start = i + 1
        return stack[0] + s[start:]
