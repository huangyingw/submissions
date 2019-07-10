

class Solution(object):
    def shortestToChar(self, s, c):

        prev = float('-inf')
        ans = []
        for i in range(len(s)):
            if s[i] == c:
                prev = i
            ans.append(i - prev)
        prev = float('inf')
        for i in range(len(s) - 1, -1, -1):
            if s[i] == c:
                prev = i
            ans[i] = min(ans[i], prev - i)
        return ans
