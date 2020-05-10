class Solution(object):
    def repeatedSubstringPattern(self, s):
        for i in range(len(s) // 2, 1, -1):
            if len(s) % i == 0:
                result = ""
                for j in range(len(s) // i):
                    newStr = s[0:i]
                    result += newStr
        return s == result
