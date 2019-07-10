_author_ = 'jake'
_project_ = 'leetcode'













from collections import defaultdict


class Solution(object):
    def findBlackPixel(self, picture, N):

        pixels = 0
        rows, cols = len(picture), len(picture[0])
        col_counts = [0 for _ in range(cols)]
        row_strings = defaultdict(int)
        for r in range(rows):
            row_count = 0
            for c in range(cols):
                if picture[r][c] == "B":
                    col_counts[c] += 1
                    row_count += 1
            if row_count == N:
                row_strings["".join(picture[r])] += 1
        for row_string in row_strings:
            if row_strings[row_string] == N:
                for i, col in enumerate(row_string):
                    if col == "B" and col_counts[i] == N:
                        pixels += N
        return pixels
