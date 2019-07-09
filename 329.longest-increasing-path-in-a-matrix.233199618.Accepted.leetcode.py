class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        result = 0
        dp = [[0 for col in range(len(matrix[0]))] for row in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                result = max(result, self.dfs(matrix, dp, row, col))
        return result

    def dfs(self, matrix, dp, i, j):
        if dp[i][j]:
            return dp[i][j]
        max_depth = 0
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for d in direction:
            x, y = i + d[0], j + d[1]
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] < matrix[i][j]:
                max_depth = max(max_depth, self.dfs(matrix, dp, x, y))
        dp[i][j] = max_depth + 1
        return dp[i][j]
