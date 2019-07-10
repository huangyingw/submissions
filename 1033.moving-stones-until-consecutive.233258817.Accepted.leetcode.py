_author_ = 'jake'
_project_ = 'leetcode'


















class Solution(object):
    def numMovesStones(self, a, b, c):

        stones = sorted([a, b, c])
        gap1, gap2 = stones[1] - stones[0] - 1, stones[2] - stones[1] - 1
        min_moves = 1 if gap1 == 1 or gap2 == 1 else int(gap1 > 0) + int(gap2 > 0)
        max_moves = gap1 + gap2
        return [min_moves, max_moves]
