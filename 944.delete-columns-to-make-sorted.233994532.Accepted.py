_author_ = 'jake'
_project_ = 'leetcode'















class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        deletions = 0
        for col in zip(*A):
            if list(col) != sorted(col):
                deletions += 1
        return deletions
