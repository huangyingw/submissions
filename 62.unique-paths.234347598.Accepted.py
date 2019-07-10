class Solution:
    def uniquePaths(self, m, n):












        if m > n:
            return self.uniquePaths(n, m)
        curr = [1] * m
        for j in range(1, n):
            for i in range(1, m):
                curr[i] += curr[i - 1]
        return curr[m - 1]
