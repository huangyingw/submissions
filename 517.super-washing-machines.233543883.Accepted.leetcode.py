class Solution(object):
    def findMinMoves(self, machines):
        dresses = sum(machines)
        if dresses % len(machines) != 0:
            return -1
        target = dresses / len(machines)
        moves, running = 0, 0
        machines = [m - target for m in machines]
        for machine in machines:
            running += machine
            moves = max(moves, abs(running), machine)
        return moves
