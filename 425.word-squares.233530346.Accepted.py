_author_ = 'jake'
_project_ = 'leetcode'








from collections import defaultdict


class Solution(object):
    def wordSquares(self, words):

        prefixes = defaultdict(list)
        for word in words:
            for i in range(1, len(word)):
                prefixes[word[:i]].append(word)
        squares = []
        for word in words:
            self.build_square([word], prefixes, squares)
        return squares

    def build_square(self, partial, prefixes, squares):
        if len(partial) == len(partial[0]):
            squares.append(list(partial))
            return
        prefix = []
        col = len(partial)
        for row in range(len(partial)):
            prefix.append(partial[row][col])
        next_words = prefixes["".join(prefix)]
        for next_word in next_words:
            partial.append(next_word)
            self.build_square(partial, prefixes, squares)
            partial.pop()
