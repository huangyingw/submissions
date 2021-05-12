class Solution(object):
    def findBestValue(self, arr, target):
        low, high = 0, max(arr)

        def ceiling(x):
            return sum(min(a, x) for a in arr)
        while low < high:
            mid = (low + high) // 2
            value = ceiling(mid) - target
            if value >= 0:
                high = mid
            else:
                low = mid + 1
        value = ceiling(low) - target
        lower = ceiling(low - 1) - target
        return low - 1 if abs(lower) <= abs(value) else low
