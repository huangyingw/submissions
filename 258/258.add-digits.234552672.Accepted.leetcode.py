class Solution(object):
    def addDigits(self, num):
        if num < 10:
            return num
        return num % 9 if num % 9 != 0 else 9
