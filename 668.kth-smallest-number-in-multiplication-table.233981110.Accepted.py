_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def findKthNumber(self, m, n, k):

        if m > n:
            m, n = n, m

        def helper(guess):
            count = 0
            for i in range(1, m + 1):
                temp = guess // i
                if temp > n:
                    count += n
                else:
                    count += temp
                if count >= k:
                    return True
            return False
        left, right = 1, m * n
        while left < right:
            mid = (left + right) // 2
            if helper(mid):
                right = mid
            else:
                left = mid + 1
        return left
