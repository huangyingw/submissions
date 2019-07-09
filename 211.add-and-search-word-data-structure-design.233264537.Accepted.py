_author_ = 'jake'
_project_ = 'leetcode'










from collections import defaultdict


class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.words = defaultdict(list)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.words[len(word)].append(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        for w in self.words[len(word)]:
            for i, c in enumerate(w):
                if word[i] != '.' and word[i] != c:
                    break
            else:
                return True
        return False
