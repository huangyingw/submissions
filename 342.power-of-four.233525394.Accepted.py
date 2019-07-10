_author_ = 'jake'
_project_ = 'leetcode'





import math


class Solution(object):
    def isPowerOfFour(self, num):

        if num <= 0:
            return False
        return 4 ** int(math.log(num, 4)) == num
