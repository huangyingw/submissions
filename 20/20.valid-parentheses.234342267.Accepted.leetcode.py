class Solution(object):
    def isValid(self, s):

        maps = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for c in s:
            if c in maps:
                stack.append(c)
            elif not stack:
                return False
            elif maps[stack.pop()] != c:
                return False
        return not stack
