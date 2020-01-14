import bisect
import math
class Solution(object):
    def numPrimeArrangements(self, n):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        prime_count = bisect.bisect_right(primes, n)
        return (math.factorial(prime_count) * math.factorial(n - prime_count)) % (10 ** 9 + 7)
