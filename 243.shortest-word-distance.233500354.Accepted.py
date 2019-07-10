












class Solution(object):
    def shortestDistance(self, words, word1, word2):

        shortest = len(words)
        i_1, i_2 = float("-inf"), float("-inf")
        for i, word in enumerate(words):
            if word == word1:
                i_1 = i
                shortest = min(shortest, i_1 - i_2)
            if word == word2:
                i_2 = i
                shortest = min(shortest, i_2 - i_1)
        return shortest
