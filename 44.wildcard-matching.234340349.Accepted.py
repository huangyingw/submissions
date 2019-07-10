class Solution(object):
    def isMatch(self, s, p):

        prev = [True]
        for i in range(len(p)):
            prev.append(prev[i] and p[i] == '*')
        for i in range(len(s)):
            curr = [False]
            for j in range(len(p)):
                if p[j] == "*":
                    curr.append(curr[j] or prev[j + 1])
                else:
                    curr.append(prev[j] and p[j] in [s[i], '?'])
            prev = curr
        return prev[-1]
