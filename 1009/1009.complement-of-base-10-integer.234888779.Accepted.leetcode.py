class Solution(object):
    def bitwiseComplement(self, N):
        if N == 0:
            return 1
        import math
        bits = (int)(math.floor(math.log(N) // math.log(2))) + 1
        return ((1 << bits) - 1) ^ N
