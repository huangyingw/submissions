class Solution(object):
    def isIsomorphic(self, s, t):
        s_to_t = {}
        t_to_s = {}
        for idx in range(len(s)):
            if s[idx] not in s_to_t:
                s_to_t[s[idx]] = t[idx]
            elif s_to_t[s[idx]] != t[idx]:
                return False
            if t[idx] not in t_to_s:
                t_to_s[t[idx]] = s[idx]
            elif t_to_s[t[idx]] != s[idx]:
                return False
        return True
