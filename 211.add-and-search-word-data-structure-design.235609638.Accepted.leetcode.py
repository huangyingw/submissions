class WordDictionary(object):
    def __init__(self):
        self.word_store = collections.defaultdict(list)
    def addWord(self, word):
        self.word_store[len(word)].append(word)
    def search(self, word):
        word_len = len(word)
        if '.' not in word:
            return word in self.word_store[len(word)]
        else:
            for item in self.word_store[word_len]:
                for alpha in range(0, word_len):
                    if word[alpha] != "." and word[alpha] != item[alpha]:
                        break
                    if alpha == (word_len - 1):
                        return True
            return False
