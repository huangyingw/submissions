_author_ = 'jake'
_project_ = 'leetcode'











from collections import defaultdict


class Solution:
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        rows, cols = set(), set()
        for r, c in points:
            rows.add(r)
            cols.add(c)
        row_to_cols = defaultdict(list)
        if len(rows) > len(cols):
            for r, c in points:
                row_to_cols[r].append(c)
        else:
            for r, c in points:
                row_to_cols[c].append(r)
        result = float("inf")
        col_pair_to_row = {}
        for r in sorted(row_to_cols):
            columns = sorted(row_to_cols[r])
            for i, c1 in enumerate(columns[:-1]):
                for c2 in columns[i + 1:]:
                    if (c1, c2) in col_pair_to_row:
                        result = min(result, (r - col_pair_to_row[c1, c2]) * (c2 - c1))
                    col_pair_to_row[c1, c2] = r
        return 0 if result == float('inf') else result
