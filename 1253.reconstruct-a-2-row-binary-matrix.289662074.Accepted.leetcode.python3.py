class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        n = len(colsum)
        upper_row, lower_row = [0] * n, [0] * n
        for i, col in enumerate(colsum):
            if col == 2:
                lower -= 1
                upper -= 1
                upper_row[i] = lower_row[i] = 1
            elif col == 1 and upper > lower:
                upper -= 1
                upper_row[i] = 1
            elif col == 1 and upper <= lower:
                lower -= 1
                lower_row[i] = 1
            if upper < 0 or lower < 0:
                return []
        if upper > 0 or lower > 0:
            return []
        return [upper_row, lower_row]
