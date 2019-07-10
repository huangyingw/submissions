_author_ = 'jake'
_project_ = 'leetcode'







import math


class Solution(object):
    def checkPerfectNumber(self, num):

        if num <= 1:
            return False
        sum_divisors = 1
        for i in range(2, int(math.sqrt(num)) + 1):
            div, mod = divmod(num, i)
            if mod == 0:
                sum_divisors += i + div
        return sum_divisors == num
