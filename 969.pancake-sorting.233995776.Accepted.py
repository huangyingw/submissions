_author_ = 'jake'
_project_ = 'leetcode'














class Solution:
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        flips = []
        for unsorted in range(len(A), 0, -1):
            i = A.index(unsorted)
            if i == unsorted - 1:
                continue
            A = A[unsorted - 1:i:-1] + A[:i + 1] + A[unsorted:]
            flips += [i + 1, unsorted]
        return flips
