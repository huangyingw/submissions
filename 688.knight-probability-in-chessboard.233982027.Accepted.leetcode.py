class Solution(object):
    def knightProbability(self, N, K, r, c):
        M = N // 2
        if N % 2 == 1:
            M += 1
        def convert(r1, c1):
            if r1 >= M:
                r1 = N - 1 - r1
            if c1 >= M:
                c1 = N - 1 - c1
            return [r1, c1]
        probs = [[1 for _ in range(M)] for _ in range(M)]
        for _ in range(K):
            new_probs = [[0 for _ in range(M)] for _ in range(M)]
            for r1 in range(M):
                for c1 in range(M):
                    prob = 0
                    for dr in [2, 1, -1, -2]:
                        for dc in [3 - abs(dr), abs(dr) - 3]:
                            if 0 <= r1 + dr < N and 0 <= c1 + dc < N:
                                r2, c2 = convert(r1 + dr, c1 + dc)
                                prob += probs[r2][c2] / 8.0
                    new_probs[r1][c1] = prob
            probs = new_probs
        r, c = convert(r, c)
        return probs[r][c]
