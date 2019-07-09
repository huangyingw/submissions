
from collections import defaultdict


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        n = len(tickets)
        trips = defaultdict(list)
        for x in tickets:
            trips[x[0]].append(x[1])
        for x in trips:
            trips[x].sort()
        iter = ["JFK"]

        def dfs(curr_iter):
            if len(curr_iter) == n + 1:
                return curr_iter
            curr_stop = curr_iter[-1]
            if trips[curr_stop] == []:
                return None
            next_stops = trips[curr_stop]
            i = 0
            for stop in next_stops:
                curr_iter.append(stop)
                del trips[curr_stop][i]
                if dfs(curr_iter):
                    return curr_iter
                curr_iter.pop()
                trips[curr_stop].insert(i, stop)
                i += 1
            return None
        return dfs(iter)
