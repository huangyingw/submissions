











class Solution(object):
    def minDistance(self, word1, word2):

        def edit_distance(i, j):
            if i < 0 or j < 0:
                return i + 1 + j + 1
            if (i, j) in memo:
                return memo[(i, j)]
            if word1[i] == word2[j]:
                result = edit_distance(i - 1, j - 1)
            else:
                result = 1 + min(edit_distance(i - 1, j),
                                 edit_distance(i, j - 1),
                                 edit_distance(i - 1, j - 1))
            memo[(i, j)] = result
            return result
        memo = {}
        return edit_distance(len(word1) - 1, len(word2) - 1)
