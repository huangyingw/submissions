_author_ = 'jake'
_project_ = 'leetcode'










from collections import defaultdict


class ValidWordAbbr(object):
    def __init__(self, dictionary):

        self.dictionary = set(dictionary)
        self.freq = defaultdict(int)
        for word in self.dictionary:
            self.freq[self.abbreviate(word)] += 1

    def isUnique(self, word):

        abbr = self.abbreviate(word)
        if word in self.dictionary:
            return self.freq[abbr] == 1
        else:
            return abbr not in self.freq

    def abbreviate(self, word):
        n = len(word)
        if n < 3:
            return word
        return word[0] + str(n - 2) + word[-1]
