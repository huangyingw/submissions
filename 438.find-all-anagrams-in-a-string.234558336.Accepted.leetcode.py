import collections
class Solution(object):
    def findAnagrams(self, s, p):
        pCount = collections.Counter(p)
        window = collections.Counter(s[:len(p)])
        res = []
        for i in range(len(s) - len(p)):
            if window == pCount:
                res.append(i)
            window[s[i]] -= 1
            if window[s[i]] == 0:
                del window[s[i]]
            window[s[i + len(p)]] += 1
        if window == pCount:
            res.append(len(s) - len(p))
        return res
