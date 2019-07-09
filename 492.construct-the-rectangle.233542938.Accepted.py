_author_ = 'jake'
_project_ = 'leetcode'














class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        side = int(area ** 0.5)
        while area % side != 0:
            side -= 1
        return [area // side, side]
