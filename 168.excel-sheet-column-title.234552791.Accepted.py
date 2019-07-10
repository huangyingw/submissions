

class Solution(object):
    def convertToTitle(self, n):
        col = []
        while n:
            n = n - 1
            col.append(chr((n % 26) + 65))
            n = n // 26
        return "".join(col[::-1])
