_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def preimageSizeFZF(self, K):

        def factorial_zeros(n):
            factor = 5
            result = 0
            while factor <= n:
                result += n // factor
                factor *= 5
            return result
        left, right = 0, 10 * K
        while left < right:
            mid = (left + right) // 2
            mid_zeros = factorial_zeros(mid)
            if mid_zeros < K:
                left = mid + 1
            else:
                right = mid
        return 5 if factorial_zeros(right) == K else 0
