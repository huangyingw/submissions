_author_ = 'jake'
_project_ = 'leetcode'












from collections import Counter


class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if A == B:
            return any(count > 1 for count in Counter(A).values())
        diffs = [i for i in range(len(A)) if A[i] != B[i]]
        if len(diffs) != 2:
            return False
        return A[diffs[0]] == B[diffs[1]] and A[diffs[1]] == B[diffs[0]]
