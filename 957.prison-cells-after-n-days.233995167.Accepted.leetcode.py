class Solution(object):
    def prisonAfterNDays(self, cells, N):
        day = 0
        state = tuple(cells)
        state_to_day = {}
        def next_state(state):
            return tuple([0] + [int(not (state[i - 1] ^ state[i + 1])) for i in range(1, 7)] + [0])
        while day < N and state not in state_to_day:
            state_to_day[state] = day
            day += 1
            state = next_state(state)
        if day < N:
            cycle = day - state_to_day[state]
            remaining = (N - state_to_day[state]) % cycle
            for _ in range(remaining):
                state = next_state(state)
        return list(state)
