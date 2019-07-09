_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while True:
            mid = (low + high) // 2
            g = guess(mid)
            if g == -1:
                high = mid - 1
            elif g == 1:
                low = mid + 1
            else:
                return mid
