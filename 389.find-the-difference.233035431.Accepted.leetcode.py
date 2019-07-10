class Solution(object):
    def findTheDifference(self, s, t):

        res = ord(t[-1])
        for i in range(len(s)):
            res += ord(t[i])
            res -= ord(s[i])
        return chr(res)
