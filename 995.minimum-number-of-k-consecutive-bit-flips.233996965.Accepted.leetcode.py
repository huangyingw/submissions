from collections import deque
class Solution(object):
    def minKBitFlips(self, A, K):
        flips = 0
        flip_i = deque()
        for i in range(len(A)):
            while flip_i and flip_i[0] + K <= i:
                flip_i.popleft()
            if (A[i] + len(flip_i)) % 2 == 0:
                if i > len(A) - K:
                    return -1
                flips += 1
                flip_i.append(i)
        return flips
