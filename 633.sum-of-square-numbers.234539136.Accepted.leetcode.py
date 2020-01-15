class Solution:
    def judgeSquareSum(self, c):
        def is_square(N):
            return int(N**.5)**2 == N
        return any(is_square(c - a * a) for a in xrange(int(c**.5) + 1))

    def judgeSquareSum(self, c):
        def is_square(N):
            return int(N**.5)**2 == N
        for a in range(int(c**.5) + 1):
            if is_square(c - a * a):
                return True
        return False

    def judgeSquareSum(self, c):
        if c % 4 == 3:
            return False
        i = 2
        s = 0
        while i * i <= c:
            s = 0
            while c % i == 0:
                if i % 4 == 3:
                    s += 1
                c //= i
            i += 1
            if s % 2 == 1:
                return False
        if c > 1 and c % 4 == 3:
            return False
        return True
