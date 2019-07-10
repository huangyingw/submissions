class Solution:
    def firstBadVersion(self, n):
        low = 1
        high = n
        while low < high:
            mid = low + (high - low) // 2
            if not isBadVersion(mid):
                low = mid + 1
            else:
                high = mid
        return high
