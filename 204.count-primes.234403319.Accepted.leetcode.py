class Solution:
    def countPrimes(self, n):
        def isPrime(num):
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True
        if n < 3:
            return 0
        count = 1
        for i in range(3, n, 2):
            if isPrime(i):
                count += 1
        return count
    def countPrimes(self, n):
        if n < 2:
            return 0
        s = [1] * n
        s[0] = s[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if s[i] == 1:
                s[i * i:n:i] = [0] * len(s[i * i:n:i])
        return sum(s)
