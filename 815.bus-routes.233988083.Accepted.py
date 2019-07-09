_author_ = 'jake'
_project_ = 'leetcode'













from collections import defaultdict


class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        routes = [set(route) for route in routes]
        stop_to_routes = defaultdict(set)
        for route, stops in enumerate(routes):
            for stop in stops:
                stop_to_routes[stop].add(route)
        front, back = {S}, {T}
        visited = set()
        buses = 0
        while front and back and not (front & back):
            if len(front) < len(back):
                front, back = back, front
            buses += 1
            new_front = set()
            visited |= front
            for stop in front:
                for route in stop_to_routes[stop]:
                    new_front |= routes[route]
            front = new_front - visited
        return buses if front & back else -1
