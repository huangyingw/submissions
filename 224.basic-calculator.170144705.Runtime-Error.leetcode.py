class Solution(object):
    def calculate(self, s):
        result = 0
        stack = []

        for idx, val in enumerate(s):
            if val.isdigit():
                num = ord(val)

                while idx + 1 < len(s) and s[idx + 1].isdigit():
                    num = num * 10 + ord(s[idx + 1])
                    idx += 1

                result += stack.pop() * num
            elif val in ['(', '+']:
                stack.append(stack[-1])
            elif val == ')':
                stack.pop()
            elif val == '-':
                stack.append(-1 * stack[-1])

        return result
