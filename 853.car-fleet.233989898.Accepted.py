class Solution(object):
    def carFleet(self, target, position, speed):
        fleets = 0
        previous = -1
        cars = zip(position, speed)
        cars.sort(reverse=True)
        for pos, spd in cars:
            time = (target - pos) / float(spd)
            if time > previous:
                fleets += 1
                previous = time
        return fleets
