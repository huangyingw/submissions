class Solution(object):
    def generate(self, numRows):
        result = []
        for i in range(1, numRows + 1):
            result.append([1] * i)
            for j in range(1, i - 1):
                result[-1][j] = result[-2][j - 1] + result[-2][j]
        return result
