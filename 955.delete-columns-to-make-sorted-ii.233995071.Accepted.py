_author_ = 'jake'
_project_ = 'leetcode'
















class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        rows, cols = len(A), len(A[0])
        cols_deleted = 0
        rows_to_check = {row for row in range(1, rows)}
        for col in range(cols):
            new_checks = set(rows_to_check)
            for row in rows_to_check:
                char = A[row][col]
                prev_char = A[row - 1][col]
                if char < prev_char:
                    cols_deleted += 1
                    break
                elif char > prev_char:
                    new_checks.remove(row)
            else:
                if not new_checks:
                    break
                rows_to_check = new_checks
        return cols_deleted
