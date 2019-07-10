







class Solution(object):
    def isPerfectSquare(self, num):

        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == num:
                return True
            if square > num:
                right = mid - 1
            else:
                left = mid + 1
        return False
