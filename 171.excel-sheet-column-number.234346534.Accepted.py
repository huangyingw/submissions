class Solution:
    def titleToNumber(self, s):

        result, start = 0, ord('A')
        for c in s:
            result = result * 26 + (ord(c) - start) + 1
        return result
