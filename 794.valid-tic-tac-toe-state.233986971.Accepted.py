_author_ = 'jake'
_project_ = 'leetcode'

















class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        counts, lines = [0, 0], [0, 0]
        for i, char in enumerate(("O", "X")):
            for j, row in enumerate(board):
                if row == char * 3:
                    lines[i] += 1
                if board[0][j] == board[1][j] == board[2][j] == char:
                    lines[i] += 1
                for c in row:
                    if c == char:
                        counts[i] += 1
            if board[0][0] == board[1][1] == board[2][2] == char:
                lines[i] += 1
            if board[2][0] == board[1][1] == board[0][2] == char:
                lines[i] += 1
        if lines[0] and lines[1]:
            return False
        if lines[0] and counts[0] != counts[1]:
            return False
        if lines[1] and counts[1] != counts[0] + 1:
            return False
        if counts[1] - counts[0] > 1 or counts[1] - counts[0] < 0:
            return False
        return True
