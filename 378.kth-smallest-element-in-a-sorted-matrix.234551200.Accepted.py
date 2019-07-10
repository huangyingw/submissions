
from Queue import PriorityQueue


class Solution(object):
    def kthSmallest(self, matrix, k):

        p = PriorityQueue()
        row = len(matrix)
        for c in range(row):
            p.put((matrix[0][c], 0, c))
        for i in range(k - 1):
            val, r, c = p.get()
            if r == row - 1:
                continue
            p.put((matrix[r + 1][c], r + 1, c))
        val, r, c = p.get()
        return val
