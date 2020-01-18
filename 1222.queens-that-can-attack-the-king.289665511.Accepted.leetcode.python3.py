class Solution(object):
    def queensAttacktheKing(self, queens, king):
        queen_set = {tuple(queen) for queen in queens}
        result = []
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
            r, c = king
            while 0 <= r + dr < 8 and 0 <= c + dc < 8:
                r += dr
                c += dc
                if (r, c) in queen_set:
                    result.append([r, c])
                    break
        return result
