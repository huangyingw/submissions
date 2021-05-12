class Solution(object):
    def findPermutation(self, s):
        permutation, stack = [], []
        for i in range(1, len(s) + 1):
            stack.append(i)
            if s[i - 1] == "I":
                while stack:
                    permutation.append(stack.pop())
        stack.append(len(s) + 1)
        while stack:
            permutation.append(stack.pop())
        return permutation
