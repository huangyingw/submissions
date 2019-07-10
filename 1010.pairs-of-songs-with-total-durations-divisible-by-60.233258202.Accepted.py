_author_ = 'jake'
_project_ = 'leetcode'









from collections import defaultdict


class Solution(object):
    def numPairsDivisibleBy60(self, time):

        mod_count = defaultdict(int)
        for t in time:
            mod_count[t % 60] += 1
        pairs = mod_count[0] * (mod_count[0] - 1) // 2
        pairs += mod_count[30] * (mod_count[30] - 1) // 2
        for t in range(1, 30):
            pairs += mod_count[t] * mod_count[60 - t]
        return pairs
