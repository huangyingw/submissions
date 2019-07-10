_author_ = 'jake'
_project_ = 'leetcode'











from collections import defaultdict


class Solution(object):
    def longestWord(self, words):

        length_to_words = defaultdict(set)
        for word in words:
            length_to_words[len(word)].add(word)
        candidates = {""}
        length = 0
        while True:
            next_candidates = set()
            for longer_word in length_to_words[length + 1]:
                if longer_word[:-1] in candidates:
                    next_candidates.add(longer_word)
            if not next_candidates:
                return sorted(list(candidates))[0]
            length += 1
            candidates = next_candidates
