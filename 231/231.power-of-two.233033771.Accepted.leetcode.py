class Solution(object):
    def isPowerOfTwo(self, n):
        if n < 0:
            return False
        bin_str = bin(n)
        return sum(map(lambda x: int(x), list(bin_str[2:]))) == 1
