










class Solution(object):
    def maxCount(self, m, n, ops):

        max_r, max_c = m, n
        for r, c in ops:
            max_r = min(max_r, r)
            max_c = min(max_c, c)
        return max_r * max_c
