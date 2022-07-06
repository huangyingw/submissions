class Solution(object):
    def isMatch(self, s, p):

        prev = [True]
        for j in range(len(p)):
            prev.append(p[j] == '*' and prev[j - 1])
        for i in range(len(s)):
            curr = [False]
            for j in range(len(p)):
                if p[j] == '*':
                    curr.append(curr[j - 1] or (prev[j + 1] and p[j - 1] in (s[i], '.')))
                else:
                    curr.append(prev[j] and p[j] in (s[i], '.'))
            prev = curr
        return prev[-1]
