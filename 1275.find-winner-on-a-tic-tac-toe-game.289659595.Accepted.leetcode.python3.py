class Solution(object):
    def tictactoe(self, moves):
        A, B = 1, -1
        player = A
        row_sums, col_sums = [0 for _ in range(3)], [0 for _ in range(3)]
        up_diag, down_diag = 0, 0
        for r, c in moves:
            row_sums[r] += player
            col_sums[c] += player
            if r == c:
                up_diag += player
            if r + c == 2:
                down_diag += player
            player = -player
        lines = row_sums + col_sums + [up_diag, down_diag]
        if any(line == 3 * A for line in lines):
            return "A"
        if any(line == 3 * B for line in lines):
            return "B"
        return "Draw" if len(moves) == 9 else "Pending"
