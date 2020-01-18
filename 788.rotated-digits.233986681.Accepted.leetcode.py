class Solution(object):
    def rotatedDigits(self, N):
        count = 0
        bad = {"3", "4", "7"}
        opposites = {"2", "5", "6", "9"}
        for i in range(1, N + 1):
            digits = set(str(i))
            if not bad.intersection(digits) and opposites.intersection(digits):
                count += 1
        return count
