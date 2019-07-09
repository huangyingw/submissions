_author_ = 'jake'
_project_ = 'leetcode'








import time


class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0:
            return ['']
        if n % 2 == 1:
            results = ['0', '1', '8']
        else:
            results = ['']
        strobo = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        for i in range(n // 2):
            results = [c + r + strobo[c] for r in results for c in strobo]
        return [result for result in results if (result[0] != '0' or n == 1)]
