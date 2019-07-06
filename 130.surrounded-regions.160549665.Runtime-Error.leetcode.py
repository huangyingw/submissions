class Solution(object):
    def dfs(self, board, row, col):
        if row < 0 or row == self.rows or col < 0 or col == self.cols:
            return
        if board[row][col] != "O":
            return
        board[row][col] = "1"
        self.dfs(board, row - 1, col)
        self.dfs(board, row + 1, col)
        self.dfs(board, row, col - 1)
        self.dfs(board, row, col + 1)

    def solve(self, board):
        self.rows = len(board)
        self.cols = len(board[0])
        queue = []
        for row in range(self.rows):
            queue.append((row, 0))
            queue.append((row, -1))
        for col in range(self.cols):
            queue.append((0, col))
            queue.append((-1, col))
        while queue:
            (row, col) = queue.pop(0)
            self.dfs(board, row, col)
        for row in range(self.rows):
            for col in range(self.cols):
                if board[row][col] == "1":
                    board[row][col] = "O"
                else:
                    board[row][col] = "X"
