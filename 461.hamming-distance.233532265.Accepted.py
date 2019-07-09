_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        hamming = 0
        while x or y:
            hamming += (x & 1) != (y & 1)
            x >>= 1
            y >>= 1
        return hamming
