_author_ = 'jake'
_project_ = 'leetcode'







class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return [[]]
        if n < k:
            return []
        without_last = self.combine(n - 1, k)
        with_last = [[n] + combo for combo in self.combine(n - 1, k - 1)]
        return with_last + without_last
