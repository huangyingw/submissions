from collections import defaultdict
class WordDictionary(object):
    def __init__(self):
        self.words = defaultdict(list)
    def addWord(self, word):
        self.words[len(word)].append(word)
    def search(self, word):
        for w in self.words[len(word)]:
            for i, c in enumerate(w):
                if word[i] != '.' and word[i] != c:
                    break
            else:
                return True
        return False
