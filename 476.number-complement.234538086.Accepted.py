class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """




        s = bin(num)[2:]
        l = len(s)
        return 2**l - 1 - num
