class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        jumbo = tomatoSlices - 2 * cheeseSlices
        if jumbo >= 0 and jumbo % 2 == 0:
            x = jumbo / 2
            y = cheeseSlices - (jumbo / 2)
            if x >= 0 and y >= 0:
                return [x, y]
            else:
                return []
        return []
