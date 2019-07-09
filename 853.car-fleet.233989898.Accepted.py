_author_ = 'jake'
_project_ = 'leetcode'
















class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
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
