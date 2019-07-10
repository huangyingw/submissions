class Solution(object):
    def isRobotBounded(self, instructions):

        start_x, start_y = 0, 0
        left, direct = 0, 0
        moves = [[0, 1], [-1, 0], [0, -1], [1, 0]]
        instructions = instructions * 4
        for instruction in instructions:
            if instruction == 'G':
                start_x += moves[direct][0]
                start_y += moves[direct][1]
            elif instruction == 'L':
                direct = (direct + 1) % 4
            elif instruction == 'R':
                direct = (direct + 3) % 4
        if(start_x == 0 and start_y == 0):
            return True
        return False
