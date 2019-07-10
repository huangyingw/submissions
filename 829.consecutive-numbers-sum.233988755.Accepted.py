_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def consecutiveNumbersSum(self, N):

        k = 1
        temp = N - ((k + 1) * k) // 2
        result = 0
        while temp >= 0:
            if temp % k == 0:
                result += 1
            k += 1
            temp = N - ((k + 1) * k) // 2
        return result
