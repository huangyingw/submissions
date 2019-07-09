_author_ = 'jake'
_project_ = 'leetcode'















from collections import defaultdict


class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        similar = defaultdict(set)
        for w1, w2 in pairs:
            similar[w1].add(w2)
        for w1, w2 in zip(words1, words2):
            if w1 == w2:
                continue
            if (w1 not in similar or w2 not in similar[w1]) and (w2 not in similar or w1 not in similar[w2]):
                return False
        return True
