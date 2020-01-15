from collections import defaultdict
import heapq


class Solution(object):
    def minCostToSupplyWater(self, n, wells, pipes):
        neighbours = defaultdict(list)
        for house1, house2, cost in pipes:
            neighbours[house1].append((house2, cost))
            neighbours[house2].append((house1, cost))
        heap = [(cost, i + 1) for i, cost in enumerate(wells)]
        heapq.heapify(heap)
        supplied = set()
        result = 0
        while len(supplied) < n:
            cost, house = heapq.heappop(heap)
            if house in supplied:
                continue
            supplied.add(house)
            result += cost
            for nbor, nbor_cost in neighbours[house]:
                if nbor not in supplied:
                    heapq.heappush(heap, (nbor_cost, nbor))
        return result
