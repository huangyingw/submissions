_author_ = 'jake'
_project_ = 'leetcode'





from collections import Counter


class Solution(object):
    def frequencySort(self, s):

        freq = Counter(s)
        pairs = [(count, c) for c, count in freq.items()]
        pairs.sort(reverse=True)
        result = []
        for count, c in pairs:
            result += [c] * count
        return "".join(result)
