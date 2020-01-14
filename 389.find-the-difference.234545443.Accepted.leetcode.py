class Solution:
    def findTheDifference(self, s, t):
        return (set(t) - set(s)).pop()
    def findTheDifference(self, s, t):
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if s.count(c) != t.count(c):
                return c
    from collections import Counter
    def findTheDifference(self, s, t):
        s_count, t_count = Counter(s), Counter(t)
        for k, v in t_count.items():
            if k not in s_count:
                return k
            if v > s_count[k]:
                return k
    def findTheDifference(self, s, t):
        diff = 0
        for i in range(len(s)):
            diff -= ord(s[i])
            diff += ord(t[i])
        diff += ord(t[-1])
        return chr(diff)
    def findTheDifference(self, s, t):
        xr = 0
        for c in s:
            xr = xr ^ ord(c)
        for c in t:
            xr = xr ^ ord(c)
        return chr(xr)
