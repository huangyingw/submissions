








class Solution(object):
    def solve(self, board):

        if not board or not board[0]:
            return
        rows, cols = len(board), len(board[0])
        to_expand = []
        for row in range(rows):
            to_expand += [(row, 0), (row, cols - 1)]
        for col in range(1, cols - 1):
            to_expand += [(0, col), (rows - 1, col)]
        while to_expand:
            row, col = to_expand.pop()
            if 0 <= row < rows and 0 <= col < cols and board[row][col] == 'O':
                board[row][col] = 'T'
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    to_expand.append((row + dr, col + dc))
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'T':
                    board[row][col] = 'O'
