_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def countPrimeSetBits(self, L, R):

        result = 0
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        for i in range(L, R + 1):
            if bin(i).count("1") in primes:
                result += 1
        return result
