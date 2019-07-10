














class MagicDictionary(object):
    def __init__(self):

        self.root = {}

    def buildDict(self, dict):

        for word in dict:
            node = self.root
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node["

    def search(self, word):

        def helper(i, mismatches, node):
            if mismatches == 2:
                return False
            if i == len(word):
                return "
            for c in node.keys():
                if c == "
                    continue
                if helper(i + 1, mismatches + (c != word[i]), node[c]):
                    return True
            return False
        return helper(0, 0, self.root)
