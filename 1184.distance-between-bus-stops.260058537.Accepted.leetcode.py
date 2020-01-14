class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        start, destination = min(start, destination), max(start, destination)
        clock_dist = sum(distance[start:destination])
        anti_clock_dist = sum(distance[:start]) + sum(distance[destination:])
        return min(clock_dist, anti_clock_dist)
