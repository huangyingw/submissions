class Solution(object):
    def isIsomorphic(self, s, t):
        sMap = {}
        tMap = {}
        for idx in range(len(s)):
            if sMap.get(s[idx], s[idx]) != t[idx] or tMap.get(t[idx], t[idx]) != s[idx]:
                return False
            sMap[s[idx]] = t[idx]
            tMap[t[idx]] = s[idx]
        return True
