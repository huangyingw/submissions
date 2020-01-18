class Solution:
    def hammingDistance(self, x, y):
        diff = x ^ y
        result = 0
        for _ in range(32):
            result += diff & 1
            diff = diff >> 1
        return result
