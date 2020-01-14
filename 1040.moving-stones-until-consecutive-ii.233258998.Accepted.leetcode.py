from collections import deque
class Solution(object):
    def numMovesStonesII(self, stones):
        n = len(stones)
        stones.sort()
        sum_gaps = stones[-1] - stones[0] - n + 1
        max_moves = sum_gaps - min(stones[1] - stones[0] - 1, stones[-1] - stones[-2] - 1)
        window = deque()
        min_moves = n
        for stone in stones:
            window.append(stone)
            while stone - window[0] >= n:
                window.popleft()
            moves = n - len(window)
            if moves == 1 and window[0] != stone - n + 1:
                moves = 2
            min_moves = min(min_moves, moves)
        return [min_moves, max_moves]
