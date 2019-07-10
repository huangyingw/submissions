


class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        cells = [[x, y] for x in range(R) for y in range(C)]
        distance = {}
        for cell in cells:
            diff = abs(cell[0] - r0) + abs(cell[1] - c0)
            if diff in distance:
                distance[diff].append(cell)
            else:
                distance[diff] = [cell]
        result = []
        for key in sorted(distance):
            for value in distance[key]:
                result.append(value)
        return result
