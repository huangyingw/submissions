class NestedInteger:
    def __init__(self, value=None):

    def isInteger(self):

    def add(self, elem):

    def setInteger(self, value):

    def getInteger(self):

    def getList(self):


class Solution:
    def deserialize(self, s):
        return eval(s)


class Solution:
    def deserialize(self, s):
        if s[0] != '[':
            return NestedInteger(int(s))
        res = NestedInteger()
        stack = [res]
        i, j = 1, 1
        while stack:
            if s[j] == '-':
                j += 1
            while s[j].isdigit():
                j += 1
            if i != j:
                stack[-1].add(int(s[i:j]))
            if s[j] == ']':
                r = stack.pop()
                if stack:
                    stack[-1].add(r)
            elif s[j] == '[':
                stack.append(NestedInteger())
            j += 1
            i = j
        return res
