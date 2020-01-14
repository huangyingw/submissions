class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        if destination < start:
            start, destination = destination, start
        start_to_dest = sum(distance[start:destination])
        circuit = sum(distance)
        return min(start_to_dest, circuit - start_to_dest)
