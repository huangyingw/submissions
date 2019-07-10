_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def imageSmoother(self, M):

        rows, cols = len(M), len(M[0])
        smoothed = [[0 for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                nbors, total = 0, 0
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        if r + dr < 0 or r + dr >= rows or c + dc < 0 or c + dc >= cols:
                            continue
                        total += M[r + dr][c + dc]
                        nbors += 1
                smoothed[r][c] = total // nbors
        return smoothed
