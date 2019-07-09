
class Solution(object):



    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            n &= n - 1
            count += 1
        return count




    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return str(bin(n)).count('1')



    def hammingWeight(self, n):
        onesCount = 0
        while n > 0:
            if n & 0x1:
                onesCount += 1
            n = n >> 1
        return onesCount
