class Solution(object):
    def generate(self, numRows):
        result = [[1]]
        for i in range(numRows - 1):
            result += [map(lambda x, y: x + y, [0] +
                           result[-1], result[-1] + [0])]
        return result
