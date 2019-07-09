_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1]
        i_2, i_3, i_5 = 0, 0, 0
        while len(ugly) < n:
            ugly.append(min(2 * ugly[i_2], 3 * ugly[i_3], 5 * ugly[i_5]))
            if ugly[-1] == 2 * ugly[i_2]:
                i_2 += 1
            if ugly[-1] == 3 * ugly[i_3]:
                i_3 += 1
            if ugly[-1] == 5 * ugly[i_5]:
                i_5 += 1
        return ugly[-1]
