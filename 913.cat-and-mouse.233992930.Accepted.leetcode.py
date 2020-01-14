from collections import defaultdict, deque
class Solution(object):
    def catMouseGame(self, graph):
        DRAW, MOUSE, CAT = 0, 1, 2
        n = len(graph)
        def parents(mouse, cat, turn):
            if turn == CAT:
                return [(new_mouse, cat, 3 - turn) for new_mouse in graph[mouse]]
            return [(mouse, new_cat, 3 - turn) for new_cat in graph[cat] if new_cat != 0]
        state_winner = defaultdict(int)
        degree = {}
        for mouse in range(n):
            for cat in range(n):
                degree[mouse, cat, MOUSE] = len(graph[mouse])
                degree[mouse, cat, CAT] = len(graph[cat]) - (0 in graph[cat])
        queue = deque()
        for i in range(n):
            for turn in [MOUSE, CAT]:
                state_winner[0, i, turn] = MOUSE
                queue.append((0, i, turn, MOUSE))
                if i > 0:
                    state_winner[i, i, turn] = CAT
                    queue.append((i, i, turn, CAT))
        while queue:
            i, j, turn, winner = queue.popleft()
            for i2, j2, prev_turn in parents(i, j, turn):
                if state_winner[i2, j2, prev_turn] is DRAW:
                    if prev_turn == winner:
                        state_winner[i2, j2, prev_turn] = winner
                        queue.append((i2, j2, prev_turn, winner))
                    else:
                        degree[i2, j2, prev_turn] -= 1
                        if degree[i2, j2, prev_turn] == 0:
                            state_winner[i2, j2, prev_turn] = turn
                            queue.append((i2, j2, prev_turn, turn))
        return state_winner[1, 2, MOUSE]
