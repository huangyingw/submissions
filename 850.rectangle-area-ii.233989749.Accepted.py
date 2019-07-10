












class Solution(object):
    def rectangleArea(self, rectangles):

        x_events = []
        for i, (x1, y1, x2, y2) in enumerate(rectangles):
            x_events.append((x1, True, i))
            x_events.append((x2, False, i))
        x_events.sort()
        area = 0
        alive = set()
        y_coverage = 0
        x_prev = 0
        for x, start, i in x_events:
            area += (x - x_prev) * y_coverage
            x_prev = x
            if start:
                alive.add(i)
            else:
                alive.discard(i)
            y_events = []
            for i in alive:
                y_events.append((rectangles[i][1], 1))
                y_events.append((rectangles[i][3], -1))
            y_events.sort()
            y_coverage = 0
            prev_y = 0
            alive_y = 0
            for y, start_y in y_events:
                if alive_y > 0:
                    y_coverage += y - prev_y
                alive_y += start_y
                prev_y = y
        return area % (10 ** 9 + 7)
