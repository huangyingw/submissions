import heapq


class Solution(object):
    def carPooling(self, trips, capacity):
        trips.sort(key=lambda x: x[1])
        dropoff = []
        for pickup, start, end in trips:
            while dropoff and dropoff[0][0] <= start:
                _, dropped = heapq.heappop(dropoff)
                capacity += dropped
            capacity -= pickup
            if capacity < 0:
                return False
            heapq.heappush(dropoff, (end, pickup))
        return True
