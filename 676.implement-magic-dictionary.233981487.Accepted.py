_author_ = 'jake'
_project_ = 'leetcode'















class MagicDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            node = self.root
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node["

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
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
