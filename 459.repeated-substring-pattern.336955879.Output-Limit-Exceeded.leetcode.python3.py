class Solution(object):
    def repeatedSubstringPattern(self, s):
        result = ""
        for i in range(len(s) // 2, 0, -1):
            if len(s) % i == 0:
                result = ""
                for j in range(len(s) // i):
                    newStr = s[0:i]
                    result += newStr
                    if s == result:
                        return True
        return False
