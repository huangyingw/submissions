_author_ = 'jake'
_project_ = 'leetcode'














class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        steps = 0
        divisor = 2
        while n > 1:
            while n % divisor == 0:
                steps += divisor
                n //= divisor
            divisor += 1
        return steps
