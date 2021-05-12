class Solution:
    def hasAlternatingBits(self, n):
        bits = bin(n)
        return all(bits[i] != bits[i + 1] for i in range(len(bits) - 1))


class Solution(object):
    def hasAlternatingBits(self, n):
        n, cur = divmod(n, 2)
        while n:
            if cur == n % 2:
                return False
            n, cur = divmod(n, 2)
        return True
