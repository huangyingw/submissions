_author_ = 'jake'
_project_ = 'leetcode'
















class Solution(object):
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
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
