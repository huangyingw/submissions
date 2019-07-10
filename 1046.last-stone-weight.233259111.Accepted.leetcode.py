_author_ = 'jake'
_project_ = 'leetcode'












import heapq


class Solution(object):
    def lastStoneWeight(self, stones):

        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            new = heapq.heappop(stones) - heapq.heappop(stones)
            if new != 0:
                heapq.heappush(stones, new)
        return -stones[0] if stones else 0
