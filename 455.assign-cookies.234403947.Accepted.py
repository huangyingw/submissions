
class Solution:
    def findContentChildren(self, g, s):

        g.sort()
        s.sort()
        i = j = 0
        res = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                res += 1
                i += 1
            j += 1
        return res
