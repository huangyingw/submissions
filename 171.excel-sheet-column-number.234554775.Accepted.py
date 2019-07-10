

class Solution(object):
    def titleToNumber(self, s):
        cn = 0
        for i in range(len(s)):
            cn += ((ord(s[-1 - i]) - 64) * (26**i))
        return cn
