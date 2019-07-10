





from collections import defaultdict


class Solution(object):
    def fourSumCount(self, A, B, C, D):

        AB = defaultdict(int)
        count = 0
        for a in A:
            for b in B:
                AB[a + b] += 1
        for c in C:
            for d in D:
                if -(c + d) in AB:
                    count += AB[-(c + d)]
        return count
