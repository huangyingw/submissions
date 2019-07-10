_author_ = 'jake'
_project_ = 'leetcode'














class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):

        mines = {(r, c) for r, c in mines}
        distances = [[0 for _ in range(N)] for _ in range(N)]
        plus = 0
        for r in range(N):
            distance = 0
            for c in range(N):
                distance = 0 if (r, c) in mines else distance + 1
                distances[r][c] = distance
            distance = 0
            for c in range(N - 1, -1, -1):
                distance = 0 if (r, c) in mines else distance + 1
                distances[r][c] = min(distances[r][c], distance)
        for c in range(N):
            distance = 0
            for r in range(N):
                distance = 0 if (r, c) in mines else distance + 1
                distances[r][c] = min(distances[r][c], distance)
            distance = 0
            for r in range(N - 1, -1, -1):
                distance = 0 if (r, c) in mines else distance + 1
                distances[r][c] = min(distances[r][c], distance)
                plus = max(plus, distances[r][c])
        return plus
