class Solution(object):
    def hammingDistance(self, x, y):
        hD = 0
        for i in bin(x ^ y):
            if i == '1':
                hD += 1
        return hD
