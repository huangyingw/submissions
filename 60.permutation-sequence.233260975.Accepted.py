_author_ = 'jake'
_project_ = 'leetcode'








from math import factorial


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        chars = [str(i) for i in range(1, n + 1)]
        permutations = factorial(n)
        k -= 1
        result = []
        while chars:
            digit = n * k // permutations
            result.append(chars[digit])
            del chars[digit]
            permutations //= n
            k -= digit * permutations
            n -= 1
        return "".join(result)
