class Solution1:
    def isRectangleOverlap(self, rec1, rec2):
        if (rec1[0] <= rec2[0] < rec1[2] or rec2[0] <= rec1[0] < rec2[2]) and (rec1[1] <= rec2[1] < rec1[3] or rec2[1] <= rec1[1] < rec2[3]):
            return True
        return False


class Solution2:
    def isRectangleOverlap(self, rec1, rec2):
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        if x1 >= x4 or x2 <= x3 or y1 >= y4 or y2 <= y3:
            return False
        else:
            return True
