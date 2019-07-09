_author_ = 'jake'
_project_ = 'leetcode'
















class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        r, c = r0, c0
        direction = 0
        result = [[r0, c0]]
        side = 1
        while len(result) < R * C:
            dr, dc = moves[direction]
            for _ in range(side):
                r += dr
                c += dc
                if 0 <= r < R and 0 <= c < C:
                    result.append([r, c])
            direction = (direction + 1) % 4
            dr, dc = moves[direction]
            for _ in range(side):
                r += dr
                c += dc
                if 0 <= r < R and 0 <= c < C:
                    result.append([r, c])
            direction = (direction + 1) % 4
            side += 1
        return result
