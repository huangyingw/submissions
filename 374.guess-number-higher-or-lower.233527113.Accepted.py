









class Solution(object):
    def guessNumber(self, n):

        low, high = 1, n
        while True:
            mid = (low + high) // 2
            g = guess(mid)
            if g == -1:
                high = mid - 1
            elif g == 1:
                low = mid + 1
            else:
                return mid
