class Solution(object):
    def checkStraightLine(self, coordinates):
        if len(coordinates) < 3:
            return True
        x_diff = coordinates[1][0] - coordinates[0][0]
        y_diff = coordinates[1][1] - coordinates[0][1]
        for x, y in coordinates[2:]:
            dx = x - coordinates[0][0]
            dy = y - coordinates[0][1]
            if x_diff * dy != y_diff * dx:
                return False
        return True
