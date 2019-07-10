









class Solution:
    def shortestSuperstring(self, A):

        N = len(A)
        overlaps = [[0] * N for _ in range(N)]
        for i, x in enumerate(A):
            for j, y in enumerate(A):
                if i != j:
                    for ans in range(min(len(x), len(y)), 0, -1):
                        if x.endswith(y[:ans]):
                            overlaps[i][j] = ans
                            break
        dp = [[0] * N for _ in range(1 << N)]
        parent = [[None] * N for _ in range(1 << N)]
        for mask in range(1, 1 << N):
            for bit in range(N):
                if (mask >> bit) & 1:
                    prev_mask = mask ^ (1 << bit)
                    if prev_mask == 0:
                        continue
                    for i in range(N):
                        if (prev_mask >> i) & 1:
                            overlap = dp[prev_mask][i] + overlaps[i][bit]
                            if overlap > dp[mask][bit]:
                                dp[mask][bit] = overlap
                                parent[mask][bit] = i
        mask = (1 << N) - 1
        i = max(range(N), key=lambda x: dp[-1][x])
        result = [A[i]]
        used = {i}
        while True:
            mask, j = mask ^ (1 << i), parent[mask][i]
            if j is None:
                break
            overlap = overlaps[j][i]
            prefix = A[j] if overlap == 0 else A[j][:-overlap]
            result.append(prefix)
            used.add(j)
            i = j
        result = result[::-1] + [A[i] for i in range(N) if i not in used]
        return "".join(result)
