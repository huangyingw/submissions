_author_ = 'jake'
_project_ = 'leetcode'














class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters.sort()
        houses.sort()
        heaters = [float("-inf")] + heaters + [float("inf")]
        i = 0
        radius = -1
        for house in houses:
            while heaters[i + 1] < house:
                i += 1
            left_distance = house - heaters[i]
            right_distance = heaters[i + 1] - house
            closest = min(left_distance, right_distance)
            radius = max(radius, closest)
        return radius
