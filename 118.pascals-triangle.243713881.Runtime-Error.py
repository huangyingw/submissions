class Solution(object):
    def generate(self, numRows):
        result = []
        for i in range(numRows):
            result += [[1] * i]
            for j in range(1, i):
                result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
                print
            print
        return result