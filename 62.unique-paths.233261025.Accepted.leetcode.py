class Solution(object):
    def uniquePaths(self, m, n):
        if m == 0 or n == 0:
            return 0
        row_paths = [1 for _ in range(n)]
        for row in range(m - 1):
            new_row_paths = [1]
            for col in range(1, n):
                new_row_paths.append(new_row_paths[-1] + row_paths[col])
            row_paths = new_row_paths
        return row_paths[-1]
