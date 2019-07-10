_author_ = 'jake'
_project_ = 'leetcode'


















from collections import namedtuple


class Solution(object):
    def expressiveWords(self, S, words):

        Groups = namedtuple("groups", ["chars", "counts"])

        def get_groups(word):
            groups = Groups(chars=[], counts=[])
            count = 1
            for i, c in enumerate(word):
                if i == len(word) - 1 or c != word[i + 1]:
                    groups.chars.append(c)
                    groups.counts.append(count)
                    count = 1
                else:
                    count += 1
            return groups
        result = 0
        S_groups = get_groups(S)
        for word in words:
            word_groups = get_groups(word)
            if word_groups.chars != S_groups.chars:
                continue
            for S_count, word_count in zip(S_groups.counts, word_groups.counts):
                if word_count > S_count:
                    break
                if word_count < S_count and S_count == 2:
                    break
            else:
                result += 1
        return result
