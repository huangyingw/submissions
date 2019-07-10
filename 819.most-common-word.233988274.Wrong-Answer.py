_author_ = 'jake'
_project_ = 'leetcode'








from collections import defaultdict


class Solution(object):
    def mostCommonWord(self, paragraph, banned):

        banned = set(banned)
        punct = {"!", "?", ",", ".", ";", "'"}
        counter = defaultdict(int)
        for word in (s.lower() for s in paragraph.split(" ")):
            word = "".join(c for c in word if c not in punct)
            if word not in banned:
                counter[word] += 1
        return max(counter.items(), key=lambda x: x[1])[0]
