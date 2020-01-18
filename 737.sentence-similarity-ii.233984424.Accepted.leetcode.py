class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        def find(word):
            if word not in mapping:
                return None
            while mapping[word] != word:
                mapping[word] = mapping[mapping[word]]
                word = mapping[word]
            return word
        if len(words1) != len(words2):
            return False
        mapping = {}
        for w1, w2 in pairs:
            p1, p2 = find(w1), find(w2)
            if p1:
                if p2:
                    mapping[p1] = p2
                else:
                    mapping[w2] = p1
            else:
                if p2:
                    mapping[w1] = p2
                else:
                    mapping[w1] = mapping[w2] = w1
        for w1, w2 in zip(words1, words2):
            if w1 == w2:
                continue
            p1, p2 = find(w1), find(w2)
            if not p1 or not p2 or p1 != p2:
                return False
        return True
