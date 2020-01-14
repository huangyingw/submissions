class Solution(object):
    def countSquares(self, matrix):
        p_arr = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        result = 0
        for index_i in range(1, len(matrix)):
            for index_j in range(1, len(matrix[0])):
                if matrix[index_i][index_j] == 1:
                    matrix[index_i][index_j] = min(matrix[index_i - 1][index_j - 1], min(matrix[index_i - 1][index_j], matrix[index_i][index_j - 1])) + 1
        return sum([sum(x) for x in matrix])
