from collections import defaultdict
class Solution(object):
    def findItinerary(self, tickets):
        tickets.sort(reverse=True)
        flights = defaultdict(list)
        for start, end in tickets:
            flights[start].append(end)
        journey = []
        def visit(airport):
            while flights[airport]:
                visit(flights[airport].pop())
            journey.append(airport)
        visit("JFK")
        return journey[::-1]
class Solution2(object):
    def findItinerary(self, tickets):
        flights = defaultdict(list)
        tickets.sort(reverse=True)
        for start, end in tickets:
            flights[start].append(end)
        route, stack = [], ['JFK']
        while stack:
            while flights[stack[-1]]:
                stack.append(flights[stack[-1]].pop())
            route.append(stack.pop())
        return route[::-1]
