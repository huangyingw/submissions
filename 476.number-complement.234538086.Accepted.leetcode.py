class Solution:
    def findComplement(self, num):
        s = bin(num)[2:]
        l = len(s)
        return 2**l - 1 - num
