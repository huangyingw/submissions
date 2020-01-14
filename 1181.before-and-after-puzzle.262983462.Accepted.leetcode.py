class Solution(object):
    def beforeAndAfterPuzzles(self, phrases):
        split_phrases = [phrase.split(" ") for phrase in phrases]
        result = set()
        for i, split_phrase1 in enumerate(split_phrases):
            for j, split_phrase2 in enumerate(split_phrases):
                if i != j and split_phrase1[-1] == split_phrase2[0]:
                    joined = " ".join(split_phrase1 + split_phrase2[1:])
                    result.add(joined)
        return sorted(result)
