from collections import defaultdict


class Solution(object):
    def numKLenSubstrNoRepeats(self, S, K):
        if K > 26 or K > len(S):
            return 0
        counts = defaultdict(int)
        repeated, result = 0, 0
        for i, c in enumerate(S):
            counts[c] += 1
            if counts[c] == 2:
                repeated += 1
            if i >= K:
                counts[S[i - K]] -= 1
                if counts[S[i - K]] == 1:
                    repeated -= 1
            if i >= K - 1:
                result += repeated == 0
        return result
