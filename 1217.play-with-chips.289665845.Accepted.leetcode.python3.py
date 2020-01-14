class Solution(object):
    def minCostToMoveChips(self, chips):
        evens, odds = 0, 0
        for chip in chips:
            if chip % 2 == 0:
                evens += 1
            else:
                odds += 1
        return min(evens, odds)
