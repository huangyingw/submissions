_author_ = 'jake'
_project_ = 'leetcode'










from collections import Counter


class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        counts = Counter(A)
        for num in sorted(counts, key=abs):
            if counts[num] > counts[num * 2]:
                return False
            counts[num * 2] -= counts[num]
        return True
