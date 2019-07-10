_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def isAlienSorted(self, words, order):

        indices = {c: i for i, c in enumerate(order)}
        prev = []
        for word in words:
            mapping = [indices[c] for c in word]
            if mapping < prev:
                return False
            prev = mapping
        return True
