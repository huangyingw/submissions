import heapq


class Solution(object):
    def minBuildTime(self, blocks, split):
        heapq.heapify(blocks)
        while len(blocks) > 1:
            heapq.heappop(blocks)
            heapq.heappush(blocks, split + heapq.heappop(blocks))
        return blocks[0]
