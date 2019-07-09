_author_ = 'jake'
_project_ = 'leetcode'







from collections import Counter
import heapq


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        freq = Counter(words)
        pairs = [(-count, word) for word, count in freq.items()]
        heapq.heapify(pairs)
        return [heapq.heappop(pairs)[1] for _ in range(k)]
