_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):

        x_overlap = min(max(0, rec1[2] - rec2[0]), max(0, rec2[2] - rec1[0]))
        if x_overlap == 0:
            return False
        return min(max(0, rec1[3] - rec2[1]), max(0, rec2[3] - rec1[1])) > 0
