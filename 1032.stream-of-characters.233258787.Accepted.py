_author_ = 'jake'
_project_ = 'leetcode'

















class StreamChecker(object):
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.root = {}
        for word in words:
            node = self.root
            for c in reversed(word):
                if c not in node:
                    node[c] = {}
                node = node[c]
            node["
        self.queries = []

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.queries.append(letter)
        node = self.root
        for c in reversed(self.queries):
            if c not in node:
                return False
            node = node[c]
            if "
                return True
        return False
