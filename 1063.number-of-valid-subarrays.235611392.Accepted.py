_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def validSubarrays(self, nums):

        result = 0
        stack = []
        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()
            stack.append(num)
            result += len(stack)
        return result
