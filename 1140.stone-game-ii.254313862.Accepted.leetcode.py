class Solution(object):
    def stoneGameII(self, piles):
        n = len(piles)
        for i in range(n - 2, -1, -1):
            piles[i] += piles[i + 1]
        memo = {}

        def helper(i, M):
            if i + 2 * M >= n:
                return piles[i]
            if (i, M) in memo:
                return memo[(i, M)]
            best = 0
            for x in range(1, 2 * M + 1):
                best = max(best, piles[i] - helper(i + x, max(M, x)))
            memo[(i, M)] = best
            return best
        return helper(0, 1)
