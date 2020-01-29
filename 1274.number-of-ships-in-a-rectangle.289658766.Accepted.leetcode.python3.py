class Solution(object):
    def countShips(self, sea, topRight, bottomLeft):
        def counter(top_right, bottom_left):
            if not sea.hasShips(top_right, bottom_left):
                return 0
            x_dist = top_right.x - bottom_left.x
            y_dist = top_right.y - bottom_left.y
            if x_dist == 0 and y_dist == 0:
                return 1
            if x_dist > y_dist:
                x_mid = bottom_left.x + x_dist / 2
                return counter(Point(x_mid, top_right.y), bottom_left) + counter(top_right,
                                                                                 Point(x_mid + 1, bottom_left.y))
            else:
                y_mid = bottom_left.y + y_dist / 2
                return counter(Point(top_right.x, y_mid), bottom_left) + counter(top_right,
                                                                                 Point(bottom_left.x, y_mid + 1))
        return counter(topRight, bottomLeft)
