class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1, d2 = [-1] * 128, [-1] * 128
        for i in range(len(s)):
            if d1[ord(s[i])] != d2[ord(t[i])]:
                return False
            d1[ord(s[i])] = i
            d2[ord(t[i])] = i
        return True

    def isIsomorphic1(self, s: str, t: str) -> bool:
        d1, d2 = {}, {}
        for i in range(len(s)):
            if d1.get(ord(s[i]), -1) != d2.get(ord(t[i]), -1):
                return False
            d1[ord(s[i])] = i
            d2[ord(t[i])] = i
        return True
