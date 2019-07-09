
class Solution:




    def isPowerOfFour(self, num):
        """
        :type n: int
        :rtype: bool
        """
        if num <= 0:
            return False
        while num > 1:
            if num % 4 == 0:
                num //= 4
            else:
                return False
        return True



    def isPowerOfFour(self, num):
        """
        :type n: int
        :rtype: bool
        """
        return (num > 0) and (num & (num - 1) == 0) and (num & 0xAAAAAAAA) == 0


    def isPowerOfFour(self, num):
        """
        :type n: int
        :rtype: bool
        """
        return num > 0 and (num == 1 or (num % 4 == 0 and self.isPowerOfFour(num / 4)))
