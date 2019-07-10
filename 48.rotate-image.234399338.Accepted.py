





class Solution:


    def rotate(self, matrix):
        matrix[::] = list(zip(*matrix[::-1]))


    def rotate(self, matrix):
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
if __name__ == '__main__':
    t = Solution()
    a = [
        [15, 13, 2, 5],
          [14, 3, 4, 1],
          [12, 6, 8, 9],
          [16, 7, 10, 11]
    ]
