_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        head = 1
        l_to_r = True
        step = 1
        while n > 1:
            if l_to_r:
                head += step
            else:
                if n % 2 != 0:
                    head += step
            step *= 2
            n //= 2
            l_to_r = not l_to_r
        return head
