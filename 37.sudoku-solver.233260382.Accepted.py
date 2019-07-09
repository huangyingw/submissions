_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.size = 9
        self.board = board
        self.new_digits = []
        for r in range(self.size):
            self.board[r] = [digit for digit in self.board[r]]
            for c in range(self.size):
                if self.board[r][c] == '.':
                    self.board[r][c] = {str(i) for i in range(1, 10)}
                else:
                    self.new_digits.append((r, c))
        while self.new_digits:
            for r, c in self.new_digits:
                self.eliminate(r, c)
                self.new_digits = []
                self.find_new()
        self.solve_recursive()

    def eliminate(self, row, col):
        for i in range(self.size):
            if isinstance(self.board[i][col], set):
                self.board[i][col].discard(self.board[row][col])
            if isinstance(self.board[row][i], set):
                self.board[row][i].discard(self.board[row][col])
        for box_row in range(3 * (row // 3), 3 + 3 * (row // 3)):
            for box_col in range(3 * (col // 3), 3 + 3 * (col // 3)):
                if isinstance(self.board[box_row][box_col], set):
                    self.board[box_row][box_col].discard(self.board[row][col])

    def find_new(self):
        for row in range(self.size):
            for col in range(self.size):
                if isinstance(self.board[row][col], set) and len(self.board[row][col]) == 1:
                    self.board[row][col] = self.board[row][col].pop()
                    self.new_digits.append((row, col))

    def solve_recursive(self):
        for r in range(self.size):
            for c in range(self.size):
                if len(self.board[r][c]) == 1:
                    continue
                for digit in self.board[r][c]:
                    if self.is_valid(r, c, digit):
                        save_set = self.board[r][c]
                        self.board[r][c] = digit
                        if self.solve_recursive():
                            return True
                        self.board[r][c] = save_set
                return False
        return True

    def is_valid(self, row, col, digit):
        for i in range(self.size):
            if self.board[row][i] == digit or self.board[i][col] == digit:
                return False
        n = self.size // 3
        for r in range(n * (row // n), n + n * (row // n)):
            for c in range(n * (col // n), n + n * (col // n)):
                if self.board[r][c] == digit:
                    return False
        return True
