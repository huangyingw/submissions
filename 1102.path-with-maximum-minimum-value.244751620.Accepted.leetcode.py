import heapq


class Solution(object):
    def maximumMinimumPath(self, A):
        rows, cols = len(A), len(A[0])
        heap = [(-A[rows - 1][cols - 1], rows - 1, cols - 1)]
        while True:
            neg_max, r, c = heapq.heappop(heap)
            if A[r][c] == - 1:
                continue
            A[r][c] = -1
            if r == c == 0:
                return -neg_max
            for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                if r + dr < 0 or r + dr >= rows or c + dc < 0 or c + dc >= cols:
                    continue
                heapq.heappush(heap, (max(-A[r + dr][c + dc], neg_max), r + dr, c + dc))
