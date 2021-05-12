class Solution(object):
    def guessNumber(self, n):
        begin, end = 1, n
        while begin <= end:
            mid = (begin + end) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res > 0:
                begin = mid + 1
            else:
                end = mid - 1
