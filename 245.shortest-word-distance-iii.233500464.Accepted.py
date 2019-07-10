







class Solution(object):
    def shortestWordDistance(self, words, word1, word2):

        last1, last2 = -1, -1
        same = word1 == word2
        distance = len(words)
        for i, word in enumerate(words):
            if word == word1:
                if same:
                    last1, last2 = last2, i
                else:
                    last1 = i
            elif word == word2:
                last2 = i
            if last1 != -1 and last2 != -1:
                distance = min(distance, abs(last1 - last2))
        return distance
