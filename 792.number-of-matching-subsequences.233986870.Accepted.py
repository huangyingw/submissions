_author_ = 'jake'
_project_ = 'leetcode'







from collections import defaultdict


class Solution(object):
    def numMatchingSubseq(self, S, words):

        letter_to_suffixes = defaultdict(list)
        letter_to_suffixes["
        result = 0
        for c in "
            suffixes = letter_to_suffixes[c]
            del letter_to_suffixes[c]
            for suffix in suffixes:
                if len(suffix) == 0:
                    result += 1
                    continue
                next_letter, next_suffix = suffix[0], suffix[1:]
                letter_to_suffixes[next_letter].append(next_suffix)
        return result
