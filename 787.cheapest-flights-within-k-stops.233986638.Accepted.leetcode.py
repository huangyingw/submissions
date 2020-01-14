from collections import defaultdict
import heapq
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        flts = defaultdict(list)
        for start, end, cost in flights:
            flts[start].append((end, cost))
        queue = [(0, -1, src)]
        visited = set()
        while queue:
            cost, stops, location = heapq.heappop(queue)
            visited.add(location)
            if location == dst:
                return cost
            if stops == K:
                continue
            for end, next_cost in flts[location]:
                if end not in visited:
                    heapq.heappush(queue, (cost + next_cost, stops + 1, end))
        return -1
