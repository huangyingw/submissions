_author_ = 'jake'
_project_ = 'leetcode'






from collections import defaultdict


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
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
