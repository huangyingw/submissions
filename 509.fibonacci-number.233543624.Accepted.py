_author_ = 'jake'
_project_ = 'leetcode'











class Solution:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        i, j = 0, 1
        for _ in range(N):
            i, j = j, i + j
        return i
