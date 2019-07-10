import random


class Solution(object):
    def __init__(self, radius, x_center, y_center):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        x, y = 2 * random.random() - 1, 2 * random.random() - 1
        if x * x + y * y > 1:
            return self.randPoint()
        return [x * self.radius + self.x_center, y * self.radius + self.y_center]

    def randPoint2(self):
        radius = random.random() ** 0.5 * self.radius
        angle = random.random() * 2 * math.pi
        return [radius * math.sin(angle) + self.x_center, radius * math.cos(angle) + self.y_center]
