













import heapq


class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):

        projects = sorted(zip(Capital, Profits))
        i = 0
        available = []
        while k > 0:
            while i < len(projects) and projects[i][0] <= W:
                heapq.heappush(available, -projects[i][1])
                i += 1
            if not available:
                return W
            best_profit = heapq.heappop(available)
            W -= best_profit
            k -= 1
        return W
