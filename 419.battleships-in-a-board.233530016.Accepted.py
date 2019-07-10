











class Solution(object):
    def countBattleships(self, board):

        if not board or not board[0]:
            return 0
        rows, cols = len(board), len(board[0])
        ships = 0
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == ".":
                    continue
                if r != 0 and board[r - 1][c] == "X":
                    continue
                if c != 0 and board[r][c - 1] == "X":
                    continue
                ships += 1
        return ships
