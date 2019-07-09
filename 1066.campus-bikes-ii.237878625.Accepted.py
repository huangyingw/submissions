_author_ = 'jake'
_project_ = 'leetcode'














import heapq


class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: int
        """
        distance = []
        for worker in workers:
            distance.append([])
            for bike in bikes:
                distance[-1].append(abs(worker[0] - bike[0]) + abs(worker[1] - bike[1]))
        heap = [(0, 0, 0)]
        heapq.heapify(heap)
        seen = set()
        while True:
            dist, used, count = heapq.heappop(heap)
            if count == len(workers):
                return dist
            if used in seen:
                continue
            seen.add(used)
            for i in range(len(bikes)):
                if not used & (1 << i):
                    heapq.heappush(heap, (dist + distance[count][i], used | (1 << i), count + 1))
