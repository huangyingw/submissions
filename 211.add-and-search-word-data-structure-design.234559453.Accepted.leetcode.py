class WordDictionary(object):
    def __init__(self):
        self.dictionary = {}
    def addWord(self, word):
        if len(word) in self.dictionary:
            self.dictionary[len(word)].append(word)
        else:
            self.dictionary[len(word)] = [word]
    def search(self, word):
        if len(word) not in self.dictionary:
            return False
        if '.' in word:
            for item in self.dictionary[len(word)]:
                if re.match(re.compile(word), item) is not None:
                    return True
            return False
        else:
            if word not in self.dictionary[len(word)]:
                return False
        return True
