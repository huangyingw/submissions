_author_ = 'jake'
_project_ = 'leetcode'

















import heapq


class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        stops = 0
        fuel = startFuel
        past_fuels = []
        stations.append([target, 0])
        for distance, station_fuel in stations:
            while fuel < distance:
                if not past_fuels:
                    return -1
                fuel -= heapq.heappop(past_fuels)
                stops += 1
            heapq.heappush(past_fuels, -station_fuel)
        return stops
