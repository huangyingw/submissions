_author_ = 'jake'
_project_ = 'leetcode'






from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):

        sorted_words = defaultdict(list)
        for word in strs:
            letter_list = [c for c in word]
            letter_list.sort()
            sorted_word = "".join(letter_list)
            sorted_words[sorted_word].append(word)
        return list(sorted_words.values())
