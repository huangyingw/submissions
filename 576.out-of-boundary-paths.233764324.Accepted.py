_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def findPaths(self, m, n, N, i, j):

        paths = 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[i][j] = 1
        for _ in range(N):
            new_dp = [[0 for _ in range(n)] for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    if r == 0:
                        paths += dp[r][c]
                    if r == m - 1:
                        paths += dp[r][c]
                    if c == 0:
                        paths += dp[r][c]
                    if c == n - 1:
                        paths += dp[r][c]
                    paths %= 10 ** 9 + 7
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        if 0 <= r + dr < m and 0 <= c + dc < n:
                            new_dp[r + dr][c + dc] += dp[r][c]
                    new_dp[r][c] %= 10 ** 9 + 7
            dp = new_dp
        return paths


class Solution2(object):
    def findPaths(self, m, n, N, i, j):
        def helper(r, c, steps):
            if steps == 0:
                return 0
            if (r, c, steps) in memo:
                return memo[(r, c, steps)]
            paths = 0
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= r + dr < m and 0 <= c + dc < n:
                    paths += helper(r + dr, c + dc, steps - 1)
                else:
                    paths += 1
                paths %= 10 ** 9 + 7
            memo[(r, c, steps)] = paths
            return paths
        memo = {}
        return helper(i, j, N)
