class Solution(object):
    def __init__(self):
        self.base = 1337

    def superPow(self, a, b):
        if b is None or len(b) == 0:
            return 1
        last_digit = b.pop()
        return self.powmod(self.superPow(a, b), 10) * self.powmod(a, last_digit) % self.base

    def powmod(self, a, k):
        a %= self.base
        result = 1
        for i in range(k):
            result = (result * a) % self.base
        return result
