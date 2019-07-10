







from collections import defaultdict


class Solution:
    def distinctSubseqII(self, S):

        total = 1
        extended = defaultdict(int)
        for c in S:
            total, extended[c] = 2 * total - extended[c], total
        total -= 1
        return total % (10 ** 9 + 7)
