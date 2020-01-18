class Solution:
    def shortestDistance(self, words, word1, word2):
        idx1, idx2 = len(words), len(words)
        result = len(words)
        for i in range(len(words)):
            if words[i] == word1:
                idx1 = i
                result = min(result, abs(idx2 - idx1))
            if words[i] == word2:
                idx2 = i
                result = min(result, abs(idx2 - idx1))
        return result
