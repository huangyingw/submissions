


class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if not words:
            return 0
        words.sort(key=len)
        dp = collections.defaultdict(int)
        result = 0
        for word in words:
            for index in range(len(word)):
                char_excluded_string = word[:index] + word[index + 1:]
                if char_excluded_string in dp:
                    dp[word] = max(dp[char_excluded_string] + 1, dp[word])
                else:
                    dp[word] = max(dp[word], 1)
            result = max(dp[word], result)
        return result
