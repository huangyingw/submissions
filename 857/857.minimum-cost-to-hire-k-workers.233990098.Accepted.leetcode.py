import heapq


class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        wage_per_quality = [(w // float(q), q) for w, q in zip(wage, quality)]
        wage_per_quality.sort()
        workers = [-q for _, q in wage_per_quality[:K]]
        heapq.heapify(workers)
        total_quality = -sum(workers)
        cost = wage_per_quality[K - 1][0] * total_quality
        for wpq, q in wage_per_quality[K:]:
            heapq.heappush(workers, -q)
            total_quality += q + heapq.heappop(workers)
            cost = min(cost, wpq * total_quality)
        return cost
