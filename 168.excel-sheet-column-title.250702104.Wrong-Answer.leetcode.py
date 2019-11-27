class Solution(object):
    def convertToTitle(self, n):
        result = ''
        while n:
            n -= 1
            temp = chr(ord('A') + (n - 1) % 26)
            result += temp
        return result
