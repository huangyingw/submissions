_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        def LCS(s, t):
            prev_dp = [0 for _ in range(len(word2) + 1)]
            for i in range(1, len(word1) + 1):
                dp = [0]
                for j in range(1, len(word2) + 1):
                    if word1[i - 1] == word2[j - 1]:
                        dp.append(1 + prev_dp[j - 1])
                    else:
                        dp.append(max(dp[-1], prev_dp[j]))
                prev_dp = dp
            return prev_dp[-1]
        return len(word1) + len(word2) - 2 * LCS(word1, word2)
