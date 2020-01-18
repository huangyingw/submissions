import heapq


class Solution(object):
    def connectSticks(self, sticks):
        cost = 0
        heapq.heapify(sticks)
        while len(sticks) > 1:
            x, y = heapq.heappop(sticks), heapq.heappop(sticks)
            cost += x + y
            heapq.heappush(sticks, x + y)
        return cost
