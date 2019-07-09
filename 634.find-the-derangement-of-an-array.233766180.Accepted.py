_author_ = 'jake'
_project_ = 'leetcode'
















class Solution(object):
    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        MODULO = 10 ** 9 + 7
        derange, one_correct = 0, 1
        for i in range(2, n + 1):
            derange, one_correct = (derange * (i - 1) + one_correct) % MODULO, (i * derange) % MODULO
        return derange
