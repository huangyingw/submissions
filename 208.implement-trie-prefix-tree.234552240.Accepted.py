
class Trie:
    def __init__(self):

        self.dic = {}

    def insert(self, word):

        cur = self.dic
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['end'] = {}

    def search(self, word):

        cur = self.dic
        for c in word:
            if c in cur:
                cur = cur[c]
            else:
                return False
        if 'end' in cur:
            return True
        return False

    def startsWith(self, prefix):

        cur = self.dic
        for c in prefix:
            if c in cur:
                cur = cur[c]
            else:
                return False
        return True
