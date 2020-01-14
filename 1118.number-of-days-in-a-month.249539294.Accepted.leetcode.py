class Solution(object):
    def numberOfDays(self, Y, M):
        if M == 2:
            if Y % 4 != 0:
                return 28
            if Y % 400 == 0:
                return 29
            if Y % 100 == 0:
                return 28
            return 29
        if M in [4, 6, 9, 11]:
            return 30
        return 31
