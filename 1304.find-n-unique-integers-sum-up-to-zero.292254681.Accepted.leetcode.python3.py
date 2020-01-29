class Solution(object):
    def sumZero(self, n):
        ints = [i for i in range(1, (n / 2) + 1)]
        ints += [-i for i in ints]
        return ints if n % 2 == 0 else ints + [0]
