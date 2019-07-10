


class Solution(object):
    def licenseKeyFormatting(self, S, K):
        S = S.replace('-', '').upper()
        result = ""
        if len(S) % K == 0:
            for index in range(0, len(S), K):
                result += S[index:index + K] + "-"
        else:
            result = S[:len(S) % K] + "-"
            for index in range(len(S) % K, len(S), K):
                result += S[index:index + K] + "-"
        return result[:-1]
