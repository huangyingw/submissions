class Solution(object):
    def generate(self, numRows):
        if numRows == 1:
            return [[1]]
        res = []
        for i in range(numRows):
            row = [1] * (i + 1)
            res.append(row)
            for j in range(1, len(row) - 1):
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
        return res
