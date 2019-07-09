_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def smallestSubsequence(self, text):
        """
        :type text: str
        :rtype: str
        """
        last_index = {c: i for i, c in enumerate(text)}
        stack = []
        for i, c in enumerate(text):
            if c in stack:
                continue
            while stack and stack[-1] > c and last_index[stack[-1]] > i:
                stack.pop()
            stack.append(c)
        return "".join(stack)
