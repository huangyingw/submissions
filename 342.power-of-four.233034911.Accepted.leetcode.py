class Solution(object):
    def isPowerOfFour(self, num):





        return num > 0 and num & (num - 1) == 0 and len(bin(num)[3:]) % 2 == 0
