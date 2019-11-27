class Solution(object):
    def isValid(self, s):
        stack = []
        match = {'(': ')', '[': ']', '{': '}'}
        for c in s:
            if c in match:
                stack.append(c)
            else:
                if not stack or match[stack.pop()] != c:
                    return False
        return not stack
