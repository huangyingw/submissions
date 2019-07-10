_author_ = 'jake'
_project_ = 'leetcode'










from collections import Counter


class Solution:
    def hasGroupsSizeX(self, deck):

        freq = Counter(deck)
        min_count = min(freq.values())
        if min_count == 1:
            return False
        for X in range(2, min_count + 1):
            if all(count % X == 0 for count in freq.values()):
                return True
        return False
