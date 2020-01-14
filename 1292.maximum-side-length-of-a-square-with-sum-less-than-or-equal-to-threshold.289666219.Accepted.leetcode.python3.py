class Solution(object):
    def maxSideLength(self, mat, threshold):
        rows, cols = len(mat), len(mat[0])
        max_side = 0
        def val_or_zero(row, col):
            return mat[row][col] if row >= 0 and col >= 0 else 0
        for r in range(rows):
            for c in range(cols):
                mat[r][c] += val_or_zero(r - 1, c) + val_or_zero(r, c - 1) - val_or_zero(r - 1, c - 1)
                if r >= max_side and c >= max_side:
                    next_side_square = val_or_zero(r, c)
                    next_side_square -= val_or_zero(r - max_side - 1, c)
                    next_side_square -= val_or_zero(r, c - max_side - 1)
                    next_side_square += val_or_zero(r - max_side - 1, c - max_side - 1)
                    if next_side_square <= threshold:
                        max_side += 1
        return max_side
