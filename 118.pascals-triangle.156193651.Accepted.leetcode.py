class Solution(object):
    def generate(self, numRows):
        result = [[1]]

        for i in range(1, numRows):
            result += [map(lambda x, y: x + y, result[-1] +
                           [0], [0] + result[-1])]
        return result[:numRows]
