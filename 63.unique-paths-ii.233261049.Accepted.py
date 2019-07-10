








class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if not m or not n:
            return 0
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0
        row_paths = [0 for _ in range(n + 1)]
        row_paths[1] = 1
        for row in range(1, m + 1):
            new_row_paths = [0]
            for col in range(1, n + 1):
                if obstacleGrid[row - 1][col - 1]:
                    new_row_paths.append(0)
                else:
                    new_row_paths.append(new_row_paths[-1] + row_paths[col])
            row_paths = new_row_paths
        return row_paths[-1]
