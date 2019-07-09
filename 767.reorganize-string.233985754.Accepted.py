_author_ = 'jake'
_project_ = 'leetcode'








import heapq
from collections import Counter


class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        freq = Counter(S)
        if any(count > (len(S) + 1) // 2 for count in freq.values()):
            return ""
        heap = [(-count, letter) for letter, count in freq.items()]
        heapq.heapify(heap)
        result = []

        def add_letter(letter, neg_count):
            result.append(letter)
            neg_count += 1
            if neg_count != 0:
                heapq.heappush(heap, (neg_count, letter))
        while heap:
            neg_count, letter = heapq.heappop(heap)
            if not result or result[-1] != letter:
                add_letter(letter, neg_count)
                continue
            if not heap:
                return ""
            neg_count2, letter2 = heapq.heappop(heap)
            add_letter(letter2, neg_count2)
            heapq.heappush(heap, (neg_count, letter))
        return "".join(result)
