_author_ = 'jake'
_project_ = 'leetcode'










from collections import defaultdict
import heapq


class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        TOP_SCORES = 5
        heaps = defaultdict(list)
        for id, score in items:
            if len(heaps[id]) < TOP_SCORES:
                heapq.heappush(heaps[id], score)
            else:
                heapq.heappushpop(heaps[id], score)
        result = [[id, sum(scores) // 5] for id, scores in heaps.items()]
        return sorted(result)
