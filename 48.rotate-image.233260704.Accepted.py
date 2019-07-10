_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def rotate(self, matrix):

        n = len(matrix)
        layers = n // 2
        for layer in range(layers):
            for i in range(layer, n - layer - 1):
                temp = matrix[layer][i]
                matrix[layer][i] = matrix[n - 1 - i][layer]
                matrix[n - 1 - i][layer] = matrix[n - 1 - layer][n - 1 - i]
                matrix[n - 1 - layer][n - 1 - i] = matrix[i][n - 1 - layer]
                matrix[i][n - 1 - layer] = temp
