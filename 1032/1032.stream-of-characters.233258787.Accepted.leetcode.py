class StreamChecker(object):
    def __init__(self, words):
        self.root = {}
        for word in words:
            node = self.root
            for c in reversed(word):
                if c not in node:
                    node[c] = {}
                node = node[c]
            node["#"] = True
        self.queries = []

    def query(self, letter):
        self.queries.append(letter)
        node = self.root
        for c in reversed(self.queries):
            if c not in node:
                return False
            node = node[c]
            if "#" in node:
                return True
        return False
