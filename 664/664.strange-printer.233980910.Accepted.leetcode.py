class Solution(object):
    def strangePrinter(self, s):
        s = "".join([a for a, b in zip(s, "#" + s) if a != b])
        memo = {}

        def helper(i, j):
            if j - i + 1 <= 1:
                return j - i + 1
            if (i, j) in memo:
                return memo[(i, j)]
            for k in range(i + 1, j + 1):
                if s[k] == s[i]:
            memo[(i, j)] = min_prints
            return min_prints
        return helper(0, len(s) - 1)
