class Solution:
    def findLength1(self, A, B):
        memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    memo[i][j] = memo[i + 1][j + 1] + 1
        return max(max(row) for row in memo)
    def findLength2(self, A, B):
        def check(length):
            seen = {A[i:i + length]
                    for i in range(len(A) - length + 1)}
            return any(B[j:j + length] in seen
                       for j in range(len(B) - length + 1))
        A = ''.join(map(chr, A))
        B = ''.join(map(chr, B))
        lo, hi = 0, min(len(A), len(B)) + 1
        while lo < hi:
            mi = (lo + hi) // 2
            if check(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo - 1
