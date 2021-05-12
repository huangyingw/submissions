class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        start = 0
        cost, result = 0, 0
        for i, (c1, c2) in enumerate(zip(s, t)):
            cost += abs(ord(c1) - ord(c2))
            while cost > maxCost:
                cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1
            result = max(result, i - start + 1)
        return result
