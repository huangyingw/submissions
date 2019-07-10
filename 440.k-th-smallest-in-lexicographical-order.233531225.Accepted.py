








class Solution(object):
    def findKthNumber(self, n, k):

        kth = 1
        k -= 1
        while k > 0:
            lower, upper = kth, kth + 1
            count = 0
            while lower <= n:
                count += min(upper, n + 1) - lower
                lower *= 10
                upper *= 10
            if count <= k:
                k -= count
                kth += 1
            else:
                k -= 1
                kth *= 10
        return kth
