class WordDictionary(object):
    def __init__(self):
        self.trie = {}

    def addWord(self, word):
        t = self.trie
        for c in word:
            t = t.setdefault(c, {})
        t[None] = None

    def search(self, word):
        return self.dfs(word, self.trie)

    def dfs(self, word, trie):
        if word == '':
            return None in trie
        c = word[0]
        if c != '.':
            return c in trie and self.dfs(word[1:], trie[c])
        return any(self.dfs(word[1:], kid) for kid in trie.values() if kid)
