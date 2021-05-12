class Solution:
    def countPrimeSetBits(self, L, R):
        return sum(map(lambda x: bin(x).count('1') in [2, 3, 5, 7, 11, 13, 17, 19], range(L, R + 1)))
