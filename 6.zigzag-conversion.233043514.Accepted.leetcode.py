class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        result = ["" for _ in range(numRows)]
        row, down = 0, 1
        for char in s:
            result[row] += char
