








class Solution(object):
    def exist(self, board, word):

        if not board or not board[0]:
            return False
        rows, cols = len(board), len(board[0])
        for r in range(rows):
            for c in range(cols):
                if self.can_find(word, 0, board, r, c):
                    return True
        return False

    def can_find(self, word, i, board, r, c):
        if i >= len(word):
            return True
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
            return False
        if word[i] != board[r][c]:
            return False
        board[r][c] = '*'
        if (self.can_find(word, i + 1, board, r + 1, c) or self.can_find(word, i + 1, board, r - 1, c) or
                self.can_find(word, i + 1, board, r, c + 1) or self.can_find(word, i + 1, board, r, c - 1)):
            return True
        board[r][c] = word[i]
        return False
