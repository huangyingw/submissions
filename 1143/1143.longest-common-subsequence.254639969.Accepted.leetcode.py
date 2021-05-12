class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        m, n = len(text1), len(text2)
        lcs = [0 for _ in range(n + 1)]
        for c1 in text1:
            new_lcs = [0]
            for j, c2 in enumerate(text2):
                if c1 == c2:
                    new_lcs.append(1 + lcs[j])
                else:
                    new_lcs.append(max(new_lcs[-1], lcs[j + 1]))
            lcs = new_lcs
        return lcs[-1]
