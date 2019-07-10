class Solution(object):
    def primePalindrome(self, N):
        def is_prime(x):
            if x < 2 or x % 2 == 0:
                return x == 2
            for i in range(3, int(x ** 0.5) + 1, 2):
                if x % i == 0:
                    return False
            return True
        if 8 <= N <= 11:
            return 11
        n = len(str(N))
        lhs = 10 ** (n // 2)
        while True:
            candidate = int(str(lhs) + str(lhs)[-2::-1])
            if candidate >= N and is_prime(candidate):
                return candidate
            lhs += 1
