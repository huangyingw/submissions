_author_ = 'jake'
_project_ = 'leetcode'
















class Solution(object):
    def floodFill(self, image, sr, sc, newColor):

        rows, cols = len(image), len(image[0])
        startColor = image[sr][sc]
        if startColor == newColor:
            return image
        stack = [(sr, sc)]
        while stack:
            r, c = stack.pop()
            if r < 0 or r >= rows or c < 0 or c >= cols:
                continue
            if image[r][c] != startColor:
                continue
            image[r][c] = newColor
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                stack.append((r + dr, c + dc))
        return image
