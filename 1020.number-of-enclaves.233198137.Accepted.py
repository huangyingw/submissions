class Solution(object):
    def numEnclaves(self, A):

        result = 0
        queue = []
        for row in range(len(A)):
            for col in range(len(A[0])):
                result += A[row][col]
                if (row * col == 0 or row == len(A) - 1 or col == len(A[0]) - 1) and A[row][col] == 1:
                    queue.append((row, col))
        x_move = [-1, 0, 1, 0]
        y_move = [0, 1, 0, -1]
        while queue:
            x, y = queue.pop(0)
            A[x][y] = 0
            result -= 1
            for xm, ym in zip(x_move, y_move):
                nx = x + xm
                ny = y + ym
                if 0 <= nx < len(A) and 0 <= ny < len(A[0]) and A[nx][ny] == 1 and (nx, ny) not in queue:
                    queue.append((nx, ny))
        return result
