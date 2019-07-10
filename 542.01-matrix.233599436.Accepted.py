_author_ = 'jake'
_project_ = 'leetcode'









from collections import deque


class Solution(object):
    def updateMatrix(self, matrix):

        rows, cols = len(matrix), len(matrix[0])
        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        frontier = deque()
        max_dist = max(rows, cols)
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 1:
                    matrix[r][c] = max_dist
                else:
                    frontier.append((r, c))
        while frontier:
            r, c = frontier.popleft()
            for dr, dc in deltas:
                if 0 <= r + dr < rows and 0 <= c + dc < cols and matrix[r][c] + 1 < matrix[r + dr][c + dc]:
                    matrix[r + dr][c + dc] = matrix[r][c] + 1
                    frontier.append((r + dr, c + dc))
        return matrix


class Solution2(object):
    def updateMatrix(self, matrix):

        rows, cols = len(matrix), len(matrix[0])
        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        unknown = set()
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 1:
                    unknown.add((r, c))
        while unknown:
            new_unknown = set()
            for r, c in unknown:
                for dr, dc in deltas:
                    if 0 <= r + dr < rows and 0 <= c + dc < cols and (r + dr, c + dc) not in unknown:
                        matrix[r][c] = matrix[r + dr][c + dc] + 1
                        break
                else:
                    new_unknown.add((r, c))
            unknown = new_unknown
        return matrix
