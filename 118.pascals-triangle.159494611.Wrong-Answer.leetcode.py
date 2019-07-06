class Solution(object):
    def generate(self, numRows):
        result = []
        for i in range(1, numRows + 1):
            result.append([1] * i)
        return result
