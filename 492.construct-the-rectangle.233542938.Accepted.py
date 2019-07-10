













class Solution(object):
    def constructRectangle(self, area):

        side = int(area ** 0.5)
        while area % side != 0:
            side -= 1
        return [area // side, side]
