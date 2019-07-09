
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """





        sum = x ^ y
        count = 0
        while sum > 0:
            sum &= sum - 1
            count += 1
        return count
