class Solution1:
    def isValidSudoku(self, board):
        return self.isRowValid(board) and self.isColumnValid(board) and self.is33CellValid(board)

    def isRowValid(self, board):
        for row in board:
            if not self.is_valid(row):
                return False
        return True

    def isColumnValid(self, board):
        for column in zip(*board):
            if not self.is_valid(column):
                return False
        return True

    def is33CellValid(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3)
                          for y in range(j, j + 3)]
                if not self.is_valid(square):
                    return False
        return True

    def is_valid(self, value):
        res = [i for i in value if i != '.']
        return len(res) == len(set(res))


class Solution2:
    def isValidSudoku(self, board):
        seen = []
        for i, row in enumerate(board):
            for j, column in enumerate(row):
                if column != '.':
                    seen += [(column, j), (i, column), (i // 3, j // 3, column)]
        return len(seen) == len({*seen})
