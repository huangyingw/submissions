_author_ = 'jake'
_project_ = 'leetcode'










class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        i = 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[i]:
                i += 1
                stack.pop()
        return i == len(popped)
