class Solution:
    def countPrimeSetBits(self, L, R):
        prime = (2, 3, 5, 7, 11, 13, 17, 19)
        count = 0
        for num in range(L, R + 1):
            if bin(num).count('1') in prime:
                count += 1
        return count
