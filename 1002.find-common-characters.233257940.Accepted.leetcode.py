_author_ = 'jake'
_project_ = 'leetcode'
from collections import Counter


class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        counts = Counter(A[0])
        for word in A[1:]:
            word_count = Counter(word)
            for c in counts:
                counts[c] = min(counts[c], word_count[c])
        result = []
        for char, count in counts.items():
            result += [char] * count
        return result
