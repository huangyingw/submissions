class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        m, n = len(str1), len(str2)
        lcs = [["" for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if str1[i] == str2[j]:
                    lcs[i + 1][j + 1] = lcs[i][j] + str1[i]
                else:
                    lcs[i + 1][j + 1] = max(lcs[i + 1][j], lcs[i][j + 1], key=len)
        result = []
        i, j = 0, 0
        for c in lcs[-1][-1]:
            while str1[i] != c:
                result.append(str1[i])
                i += 1
            while str2[j] != c:
                result.append(str2[j])
                j += 1
            result.append(c)
            i += 1
            j += 1
        return "".join(result) + str1[i:] + str2[j:]
