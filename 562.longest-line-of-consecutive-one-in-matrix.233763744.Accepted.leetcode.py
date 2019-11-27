class Solution(object):
    def longestLine(self, M):
        if not M or not M[0]:
            return 0
        rows, cols = len(M), len(M[0])
        max_len = 0
        previous_dp = [[0 for _ in range(4)] for c in range(cols)]
        for r in range(rows):
            row_dp = []
            for c in range(cols):
                if M[r][c] == 0:
                    row_dp.append([0 for _ in range(4)])
                    continue
                row_dp.append([1 for _ in range(4)])
                if c != 0:
                    row_dp[-1][0] += row_dp[-2][0]
                row_dp[-1][1] += previous_dp[c][1]
                if c != 0:
                    row_dp[-1][2] += previous_dp[c - 1][2]
                if c != cols - 1:
                    row_dp[-1][3] += previous_dp[c + 1][3]
                max_len = max(max_len, max(row_dp[-1]))
            previous_dp = row_dp
        return max_len
