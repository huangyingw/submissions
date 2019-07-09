_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if len(A) < len(B):
            A, B = B, A
        max_uncrossed = [0] * (len(B) + 1)
        for i in range(len(A)):
            new_max_uncrossed = [0]
            for j in range(len(B)):
                new_max_uncrossed.append(max(max_uncrossed[j] + int(A[i] == B[j]),
                                             max_uncrossed[j + 1], new_max_uncrossed[-1]))
            max_uncrossed = new_max_uncrossed
        return max_uncrossed[-1]
