from collections import defaultdict
import heapq
class Solution(object):
    def minimumCost(self, N, connections):
        edges = defaultdict(list)
        for a, b, cost in connections:
            edges[a].append((cost, b))
            edges[b].append((cost, a))
        connected = {1}
        connections = list(edges[1])
        heapq.heapify(connections)
        result = 0
        while len(connected) < N:
            if not connections:
                return -1
            cost, nbor = heapq.heappop(connections)
            if nbor in connected:
                continue
            connected.add(nbor)
            result += cost
            for edge in edges[nbor]:
                if edge[1] not in connected:
                    heapq.heappush(connections, edge)
        return result
