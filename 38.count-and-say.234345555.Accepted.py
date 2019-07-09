"""
Time complexity: O(n)
"""


class Solution(object):





























    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = '1'
        for i in range(n - 1):
            result = "".join(str(len(list(group))) + str(digit) for digit, group in itertools.groupby(result))
        return result
