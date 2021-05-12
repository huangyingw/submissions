class Solution(object):
    def mySqrt(self, x):
        guess = x
        while guess * guess > x:
            guess = (guess + x // guess) // 2
        return guess
