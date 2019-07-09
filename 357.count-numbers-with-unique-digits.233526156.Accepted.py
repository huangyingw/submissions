_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        uniques = 10
        can_expand = 9
        for digits in range(2, min(n, 10) + 1):
            can_expand *= (11 - digits)
            uniques += can_expand
        return uniques
