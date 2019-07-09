_author_ = 'jake'
_project_ = 'leetcode'










from collections import Counter


class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        self.total = 0
        freq = Counter(tiles)

        def helper(remaining):
            if remaining == 0:
                return
            for tile, count in freq.items():
                if count != 0:
                    freq[tile] -= 1
                    self.total += 1
                    helper(remaining - 1)
                    freq[tile] += 1
        helper(len(tiles))
        return self.total
