class Solution(object):
    def isArmstrong(self, N):
        digits = len(str(N))
        result, n = 0, N
        while n > 0:
            n, digit = divmod(n, 10)
            result += digit ** digits
        return result == N
