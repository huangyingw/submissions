class Solution(object):
    def minimumMoves(self, arr):
        memo = {}

        def dp(i, j):
            if i > j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            result = dp(i, j - 1) + 1
            if arr[j] == arr[j - 1]:
                result = min(result, dp(i, j - 2) + 1)
            for k in range(i, j - 1):
                if arr[j] == arr[k]:
                    result = min(result, dp(i, k - 1) + dp(k + 1, j - 1))
            memo[(i, j)] = result
            return result
        return dp(0, len(arr) - 1)
