_author_ = 'jake'
_project_ = 'leetcode'









from collections import Counter


class Solution(object):
    def customSortString(self, S, T):

        result = []
        t_count = Counter(T)
        for c in S:
            result += [c] * t_count[c]
            del t_count[c]
        for c, count in t_count.items():
            result += [c] * count
        return "".join(result)
