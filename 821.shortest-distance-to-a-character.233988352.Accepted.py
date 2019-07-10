











class Solution(object):
    def shortestToChar(self, S, C):

        shortest = []
        prev_C = float("-inf")
        for i, c in enumerate(S):
            if c == C:
                prev_C = i
            shortest.append(i - prev_C)
        next_C = float("inf")
        for i in range(len(S) - 1, -1, -1):
            c = S[i]
            if c == C:
                next_C = i
            shortest[i] = min(shortest[i], next_C - i)
        return shortest
