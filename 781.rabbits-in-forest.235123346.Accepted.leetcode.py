class Solution(object):
    def numRabbits(self, answers):
        colours = {}
        rabbits = 0
        for rabbit in answers:
            if colours.get(rabbit, 0) > 0:
                colours[rabbit] -= 1
            else:
                rabbits += rabbit + 1
                colours[rabbit] = rabbit
        return rabbits
