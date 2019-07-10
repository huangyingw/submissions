class Solution(object):
    def hammingDistance(self, x, y):
        hamming = 0
        while x or y:
            hamming += (x & 1) != (y & 1)
            x >>= 1
            y >>= 1
        return hamming
