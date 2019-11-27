class Solution:
    def shortestToChar(self, S, C):
        n = len(S)
        ans = [0 if i == C else n for i in S]
        for i in range(n - 1):
            ans[i + 1] = min(ans[i + 1], ans[i] + 1)
        for j in range(n - 1)[::-1]:
            ans[j] = min(ans[j], ans[j + 1] + 1)
        return ans
