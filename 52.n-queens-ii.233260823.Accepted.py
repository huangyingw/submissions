_author_ = 'jake'
_project_ = 'leetcode'








class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        partials = [[]]
        for col in range(n):
            new_partials = []
            for partial in partials:
                for row in range(n):
                    if not self.conflict(partial, row):
                        new_partials.append(partial + [row])
            partials = new_partials
        return len(partials)

    def conflict(self, partial, new_row):
        for col, row in enumerate(partial):
            if new_row == row:
                return True
            col_diff = len(partial) - col
            if row + col_diff == new_row or row - col_diff == new_row:
                return True
        return False
