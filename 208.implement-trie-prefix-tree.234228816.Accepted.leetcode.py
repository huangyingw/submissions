class TrieNode(object):
    def __init__(self):
        self.links = [None] * 26
        self.isEnd = False
    def containsKey(self, ch):
        return self.links[ord(ch) - ord('a')] != None
    def get(self, ch):
        return self.links[ord(ch) - ord('a')]
    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node
    def setEnd(self):
        self.isEnd = True
class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for i in range(len(word)):
            ch = word[i]
            if node.containsKey(ch) is False:
                node.put(ch, TrieNode())
            node = node.get(ch)
        node.setEnd()
    def searchPrefix(self, word):
        node = self.root
        for i in range(len(word)):
            ch = word[i]
            if node.containsKey(ch):
                node = node.get(ch)
            else:
                return None
        return node
    def search(self, word):
        node = self.searchPrefix(word)
        return node is not None and node.isEnd
    def startsWith(self, prefix):
        node = self.searchPrefix(prefix)
        return node is not None
