_author_ = 'jake'
_project_ = 'leetcode'










from collections import defaultdict


class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        rows, cols = len(matrix), len(matrix[0])
        if rows < cols:
            matrix = zip(*matrix[::-1])
            rows, cols = cols, rows
        cumulative_rows = []
        for row in range(rows):
            cumulative_rows.append([matrix[row][0]])
            for col in range(1, cols):
                cumulative_rows[-1].append(matrix[row][col] + cumulative_rows[-1][-1])
        result = 0
        for col_start in range(cols):
            for col_end in range(col_start, cols):
                seen = defaultdict(int, {0: 1})
                submatrix = 0
                for row in range(rows):
                    submatrix += cumulative_rows[row][col_end]
                    if col_start != 0:
                        submatrix -= cumulative_rows[row][col_start - 1]
                    if submatrix - target in seen:
                        result += seen[submatrix - target]
                    seen[submatrix] += 1
        return result
