class Solution(object):
    def isRobotBounded(self, instructions):
        r, c = 0, 0
        dr, dc = 1, 0
        for instruction in instructions:
            if instruction == "G":
                r += dr
                c += dc
            elif instruction == "L":
                dr, dc = -dc, dr
            else:
                dr, dc = dc, -dr
        return (dr, dc) != (1, 0) or (r, c) == (0, 0)
