










class TicTacToe(object):
    def __init__(self, n):

        self.rows, self.cols = [0 for _ in range(n)], [0 for _ in range(n)]
        self.d_up, self.d_down = 0, 0

    def move(self, row, col, player):

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
