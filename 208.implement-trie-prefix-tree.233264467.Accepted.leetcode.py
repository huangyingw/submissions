class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.terminal = False
class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        self.root.terminal = True
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.terminal = True
    def search(self, word):
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return node.terminal
    def startsWith(self, prefix):
        node = self.root
        for c in prefix:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return True
