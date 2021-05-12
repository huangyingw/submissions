class Solution(object):
    def movesToChessboard(self, board):
        n = len(board)
        rows = {tuple(row) for row in board}
        cols = set(zip(*board))
        moves = 0
        for patterns in [rows, cols]:
            if len(patterns) != 2:
                return -1
            p1, p2 = list(patterns)
            zero_p1, zero_p2 = sum(x == 0 for x in p1), sum(x == 0 for x in p2)
            if abs(zero_p1 - zero_p2) != n % 2 or not all(x ^ y for x, y in zip(p1, p2)):
                return -1
            p = p1 if zero_p1 > zero_p2 else p2
            p_moves = sum(x != y for x, y in zip(p, [0, 1] * ((n + 1) // 2)))
            if n % 2 == 0:
                p_moves = min(p_moves, sum(x != y for x, y in zip(p, [1, 0] * ((n + 1) // 2))))
            moves += p_moves // 2
        return moves
