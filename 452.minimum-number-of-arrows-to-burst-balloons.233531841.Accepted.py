_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def findMinArrowShots(self, points):

        arrows, last_arrow = 0, float("-inf")
        points.sort(key=lambda x: x[1])
        for start, end in points:
            if start > last_arrow:
                arrows += 1
                last_arrow = end
        return arrows
