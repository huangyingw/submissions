
class Solution(object):
    def firstUniqChar(self, s):
        res = len(s)
        for c in "abcdefghijklmnopqrstuvwxyz":
            i = s.find(c)
            if i != -1 and i == s.rfind(c):
                res = min(res, i)
        return res if res != len(s) else -1
