class Solution(object):
    def tilingRectangle(self, rows, cols):
        if cols > rows:
            cols, rows = rows, cols
        memo = {}

        def dp(state):
            if min(state) == rows:
                return 0
            if state in memo:
                return memo[state]
            min_height = min(state)
            start = state.index(min_height)
            result = cols * rows
            state_list = list(state)
            for end in range(start, cols):
                if state[end] != min_height:
                    break
                side = end - start + 1
                if min_height + side > rows:
                    break
                state_list[start: end + 1] = [min_height + side] * side
                result = min(result, dp(tuple(state_list)))
            memo[state] = result + 1
            return result + 1
        return dp(tuple([0] * cols))
