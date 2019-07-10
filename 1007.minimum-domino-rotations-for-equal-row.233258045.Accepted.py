_author_ = 'jake'
_project_ = 'leetcode'


class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n = len(A)
        for num in range(1, 7):
            if all(a == num or b == num for a, b in zip(A, B)):
                return min(n - A.count(num), n - B.count(num))
        return -1
