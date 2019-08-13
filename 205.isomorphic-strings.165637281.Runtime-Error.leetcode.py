class Solution(object):
    def isIsomorphic(self, s, t):
        sMap = {}
        tMap = {}
        for idx in range(len(s)):
            if sMap[s[idx]] != t[idx] or tMap[t[idx]] != s[idx]:
                return False
            sMap[s[idx]] = t[idx]
            tMap[t[idx]] = s[idx]
        return True
