_author_ = 'jake'
_project_ = 'leetcode'















class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        SIZE = 8
        for r in range(SIZE):
            for c in range(SIZE):
                if board[r][c] == "R":
                    start_r, start_c = r, c
                    break
        pawns = 0
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            row, col = start_r, start_c
            while True:
                row += dr
                col += dc
                if row < 0 or row >= SIZE or col < 0 or col >= SIZE:
                    break
                if board[row][col] == "B":
                    break
                if board[row][col] == "p":
                    pawns += 1
                    break
        return pawns
