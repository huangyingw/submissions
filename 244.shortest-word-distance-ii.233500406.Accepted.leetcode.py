from collections import defaultdict
class WordDistance(object):
    def __init__(self, words):
        self.word_indices = defaultdict(list)
        for i, word in enumerate(words):
            self.word_indices[word].append(i)
    def shortest(self, word1, word2):
        i1 = self.word_indices[word1]
        i2 = self.word_indices[word2]
        distance = float('inf')
        p1, p2 = 0, 0
        while p1 < len(i1) and p2 < len(i2):
            distance = min(distance, abs(i1[p1] - i2[p2]))
            if i1[p1] < i2[p2]:
                p1 += 1
            else:
                p2 += 1
        return distance
