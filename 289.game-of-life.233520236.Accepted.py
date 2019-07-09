_author_ = 'jake'
_project_ = 'leetcode'














class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        rows, cols = len(board), len(board[0])
        for r in range(rows):
            for c in range(cols):
                nbors = self.count_neighbours(r, c, board)
                if nbors == 3 or (board[r][c] and nbors == 2):
                    board[r][c] += 2
        for r in range(rows):
            for c in range(cols):
                board[r][c] >>= 1

    def count_neighbours(self, r, c, board):
        count = 0
        for row_offset in range(-1, 2):
            for col_offset in range(-1, 2):
                if row_offset == col_offset == 0:
                    continue
                if 0 <= r + row_offset < len(board) and 0 <= c + col_offset < len(board[0]):
                    count += board[r + row_offset][c + col_offset] % 2
        return count
