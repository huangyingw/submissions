class Solution(object):
    def countPrimes(self, n):
        primes = [True] * n
        i = 2
        while i * i <= n:
            if primes[i]:
                for j in range(2 * i, n, i):
                    primes[j] = False
            i += 1
        count = 0
        for prime in primes:
            if prime:
                count += 1
        return count
