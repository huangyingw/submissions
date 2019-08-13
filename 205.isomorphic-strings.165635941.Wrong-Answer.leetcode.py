class Solution(object):
    def isIsomorphic(self, s, t):
        sMap = {}
        for idx in range(len(s)):
            if s[idx] not in sMap:
                sMap[s[idx]] = t[idx]
            elif sMap[s[idx]] != t[idx]:
                return False
        return True
