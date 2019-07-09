_author_ = 'jake'
_project_ = 'leetcode'











class TicTacToe(object):
    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.rows, self.cols = [0 for _ in range(n)], [0 for _ in range(n)]
        self.d_up, self.d_down = 0, 0

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        n = len(self.rows)
        score = (2 * player) - 3
        self.rows[row] += score
        self.cols[col] += score
        if abs(self.rows[row]) == n or abs(self.cols[col]) == n:
            return player
        if row == col:
            self.d_up += score
            if abs(self.d_up) == n:
                return player
        if row + col == n - 1:
            self.d_down += score
            if abs(self.d_down) == n:
                return player
        return 0
