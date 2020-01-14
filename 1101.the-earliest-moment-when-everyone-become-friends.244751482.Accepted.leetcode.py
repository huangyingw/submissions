class Solution(object):
    def earliestAcq(self, logs, N):
        logs.sort()
        friend = {i: i for i in range(N)}
        groups = N
        def leader(i):
            while friend[i] != i:
                i = friend[i]
            return i
        for time, A, B in logs:
            a, b = leader(A), leader(B)
            if a != b:
                friend[a] = b
                groups -= 1
                if groups == 1:
                    return time
        return -1
