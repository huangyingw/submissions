


class Solution(object):
    def rotate(self, matrix):

        l = len(matrix)
        for layer in range(l // 2):
            first, last = layer, l - 1 - layer
            for i in range(first, last):
                offset = i - first
                top = matrix[first][i]
                matrix[first][i] = matrix[last - offset][first]
                matrix[last - offset][first] = matrix[last][last - offset]
                matrix[last][last - offset] = matrix[i][last]
                matrix[i][last] = top
