_author_ = 'jake'
_project_ = 'leetcode'









class Solution:
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        increments = 0
        last_used = -1
        for num in sorted(A):
            if num <= last_used:
                increments += last_used + 1 - num
                last_used += 1
            else:
                last_used = num
        return increments
