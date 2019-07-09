_author_ = 'jake'
_project_ = 'leetcode'












class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        gray = [0]
        for i in range(n):
            gray += [x + 2**i for x in reversed(gray)]
        return gray
