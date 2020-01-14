import collections
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = collections.defaultdict(dict)
        maxLength = 1
        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                dp[i][diff] = 1 + dp[j].get(diff, 1)
                maxLength = max(maxLength, dp[i][diff])
        return maxLength
class Solution1:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                diff = A[j] - A[i]
                dp[j, diff] = dp.get((i, diff), 1) + 1
        return max(dp.values())
