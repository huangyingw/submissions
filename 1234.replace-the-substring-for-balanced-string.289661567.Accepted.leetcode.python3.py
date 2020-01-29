from collections import Counter


class Solution(object):
    def balancedString(self, s):
        balance = len(s) // 4
        excess = {}
        for c, count in Counter(s).items():
            if count - balance > 0:
                excess[c] = count - balance
        if not excess:
            return 0
        start = 0
        result = len(s)
        for end, c in enumerate(s):
            if c in excess:
                excess[c] -= 1
            while all(v <= 0 for v in excess.values()):
                result = min(result, end - start + 1)
                if s[start] in excess:
                    excess[s[start]] += 1
                start += 1
        return result
