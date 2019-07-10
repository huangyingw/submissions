_author_ = 'jake'
_project_ = 'leetcode'












class Solution:
    def shortestBridge(self, A):

        rows, cols = len(A), len(A[0])
        visited = set()
        perimeter = set()

        def neighbours(r, c):
            if r != 0:
                yield (r - 1, c)
            if r != rows - 1:
                yield (r + 1, c)
            if c != 0:
                yield (r, c - 1)
            if c != rows - 1:
                yield (r, c + 1)

        def get_perimeter(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if A[r][c] == 0 or (r, c) in visited:
                return
            visited.add((r, c))
            for r1, c1 in neighbours(r, c):
                if A[r1][c1] == 0:
                    perimeter.add((r1, c1))
                else:
                    get_perimeter(r1, c1)
        for r in range(rows):
            for c in range(cols):
                if perimeter:
                    break
                get_perimeter(r, c)
        steps = 1
        while True:
            new_perimeter = set()
            for r, c in perimeter:
                for r1, c1 in neighbours(r, c):
                    if (r1, c1) in visited:
                        continue
                    if A[r1][c1] == 1:
                        return steps
                    new_perimeter.add((r1, c1))
            visited |= new_perimeter
            perimeter = new_perimeter
            steps += 1
