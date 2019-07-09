_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        boats = 0
        people.sort()
        light, heavy = 0, len(people) - 1
        while light <= heavy:
            boats += 1
            if people[light] + people[heavy] <= limit:
                light += 1
            heavy -= 1
        return boats
