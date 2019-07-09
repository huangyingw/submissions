_author_ = 'jake'
_project_ = 'leetcode'














class Solution(object):
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        result = 0
        n = len(A)
        A.sort()
        for i, num in enumerate(A):
            result += (1 << i) * num
            result -= (1 << (n - 1 - i)) * num
        return result % (10 ** 9 + 7)
