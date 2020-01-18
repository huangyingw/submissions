class Solution(object):
    def smallestCommonElement(self, mat):
        candidates = set(mat[0])
        for row in mat[1:]:
            candidates &= set(row)
        return min(candidates) if candidates else -1
