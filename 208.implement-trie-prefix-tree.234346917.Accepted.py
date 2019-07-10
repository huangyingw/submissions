class Trie:
    def __init__(self):

        self.children = {}
        self.is_word = False

    def insert(self, word):

        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.is_word = True

    def search(self, word):

        curr = self
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True if curr.is_word else False

    def startsWith(self, prefix):

        curr = self
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
