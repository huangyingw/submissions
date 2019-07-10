_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def findLonelyPixel(self, picture):

        pixels = 0
        rows, cols = len(picture), len(picture[0])
        col_counts = [0 for _ in range(cols)]
        row_pixels = [[] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if picture[r][c] == "B":
                    col_counts[c] += 1
                    row_pixels[r].append(c)
        for r in range(rows):
            if len(row_pixels[r]) == 1:
                c = row_pixels[r][0]
                if col_counts[c] == 1:
                    pixels += 1
        return pixels
