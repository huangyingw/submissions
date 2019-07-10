_author_ = 'jake'
_project_ = 'leetcode'



















class Solution(object):
    def updateBoard(self, board, click):

        r, c = click
        rows, cols = len(board), len(board[0])
        for row in range(rows):
            board[row] = [col for col in board[row]]
        if board[r][c] == "M":
            board[r][c] = "X"
            return board

        def helper(r, c):
            if board[r][c] == "B":
                return
            mines = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == dc == 0:
                        continue
                    if 0 <= r + dr < rows and 0 <= c + dc < cols and board[r + dr][c + dc] == "M":
                        mines += 1
            if mines != 0:
                board[r][c] = str(mines)
                return
            board[r][c] = "B"
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if 0 <= r + dr < rows and 0 <= c + dc < cols:
                        helper(r + dr, c + dc)
        helper(r, c)
        return board
