_author_ = 'jake'
_project_ = 'leetcode'














class Solution(object):
    def canCross(self, stones):

        jumps = {}
        for stone in stones:
            jumps[stone] = set()
        jumps[0].add(0)
        for stone in stones:
            for jump in jumps[stone]:
                for shift in [-1, 0, 1]:
                    if jump + shift > 0 and stone + jump + shift in jumps:
                        jumps[stone + jump + shift].add(jump + shift)
        return bool(jumps[stones[-1]])
