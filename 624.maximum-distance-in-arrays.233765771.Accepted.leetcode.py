class Solution(object):
    def maxDistance(self, arrays):
        low, high = arrays[0][0], arrays[0][-1]
        max_dist = 0
        for array in arrays[1:]:
            max_dist = max(max_dist, abs(array[-1] - low), abs(array[0] - high))
            low = min(low, array[0])
            high = max(high, array[-1])
        return max_dist
