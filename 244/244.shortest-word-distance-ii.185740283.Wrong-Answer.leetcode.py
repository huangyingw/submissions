class WordDistance(object):
    def __init__(self, words):
        self.w_to_idx = {}
        for idx, val in enumerate(words):
            self.w_to_idx.setdefault(val, []).append(idx)

    def shortest(self, word1, word2):
        idxs1 = self.w_to_idx[word1]
        idxs2 = self.w_to_idx[word2]