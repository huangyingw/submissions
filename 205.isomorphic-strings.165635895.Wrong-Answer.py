class Solution(object):
    def isIsomorphic(self, s, t):
        s_to_t = {}
        for idx in range(len(s)):
            if s[idx] not in s_to_t:
                s_to_t[s[idx]] = t[idx]
            elif s_to_t[s[idx]] != t[idx]:
                return False
