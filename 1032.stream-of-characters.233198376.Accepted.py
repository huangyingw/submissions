class Trie(object):
    def __init__(self):
        self.nodes = {}
        self.word = False


class StreamChecker(object):
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.trie_node = Trie()
        for word in words:
            ptr = self.trie_node
            for char in reversed(word):
                if char not in ptr.nodes:
                    ptr.nodes[char] = Trie()
                ptr = ptr.nodes[char]
            ptr.word = True
        self.stream = []

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.stream.append(letter)
        root = self.trie_node
        for char in reversed(self.stream):
            if char not in root.nodes:
                return False
            if root.nodes[char].word:
                return True
            root = root.nodes[char]
        return root.word
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
