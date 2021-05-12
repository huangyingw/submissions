class Solution(object):
    def findJudge(self, N, trust):
        if not trust:
            return 1
        d = {}
        for i in range(1, N + 1):
            d[i] = 0
        for t in trust:
            d[t[0]] += 1
            d[t[1]] -= 1
        for k, v in d.items():
            if v == -(N - 1):
                return k
        return -1
