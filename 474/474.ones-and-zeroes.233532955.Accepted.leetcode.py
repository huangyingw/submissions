class Solution(object):
    def findMaxForm(self, strs, m, n):
        max_form = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for s in strs:
            s_zeros = sum([True for c in s if c == "0"])
            s_ones = len(s) - s_zeros
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    if i >= s_zeros and j >= s_ones:
                        max_form[i][j] = max(max_form[i][j], 1 + max_form[i - s_zeros][j - s_ones])
        return max_form[-1][-1]
