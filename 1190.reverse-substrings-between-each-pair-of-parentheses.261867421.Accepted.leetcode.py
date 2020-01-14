class Solution(object):
    def reverseParentheses(self, s):
        if not s:
            return ''
        stack = []
        for char in s:
            if char == ')':
                combine_str = ''
                while stack and stack[-1] != '(':
                    elem = stack.pop()[::-1]
                    combine_str += elem
                stack.pop()
                stack.append(combine_str)
            else:
                stack.append(char)
        return "".join(stack)
