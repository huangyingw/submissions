














class Solution:
    def minDeletionSize(self, A):

        deletions = 0
        for col in zip(*A):
            if list(col) != sorted(col):
                deletions += 1
        return deletions
