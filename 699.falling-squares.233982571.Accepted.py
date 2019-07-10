_author_ = 'jake'
_project_ = 'leetcode'

















class Solution(object):
    def fallingSquares(self, positions):

        box_heights = [positions[0][1]]
        max_heights = [positions[0][1]]
        for left, side in positions[1:]:
            top = side
            for i in range(len(box_heights)):
                left2, side2 = positions[i]
                if left2 < left + side and left2 + side2 > left:
                    top = max(top, box_heights[i] + side)
            box_heights.append(top)
            max_heights.append(max(top, max_heights[-1]))
        return max_heights
