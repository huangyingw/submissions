class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        OPEN, VISITED = 1, 2
        result = 0
        open_boxes, closed_boxes = set(), set()
        for initial_box in initialBoxes:
            container = open_boxes if status[initial_box] == OPEN else closed_boxes
            container.add(initial_box)
        while open_boxes:
            for open_box in open_boxes:
                if status[open_box] == VISITED:
                    continue
                status[open_box] = VISITED
                result += candies[open_box]
                for key in keys[open_box]:
                    status[key] = OPEN
                closed_boxes.update(containedBoxes[open_box])
            open_boxes = {box for box in closed_boxes if status[box] == OPEN}
            closed_boxes -= open_boxes
        return result
