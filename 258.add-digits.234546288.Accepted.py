



class Solution:

    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while True:
            result = 0
            while num != 0:
                ind = num % 10
                num = num // 10
                result += ind
            if result < 10:
                break
            else:
                num = result
        return result


    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            num = sum(map(int, str(num)))
        return num


    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        else:
            return (num - 1) % 9 + 1
