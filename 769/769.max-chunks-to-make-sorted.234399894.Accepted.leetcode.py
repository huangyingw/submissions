class Solution:
    def maxChunksToSorted(self, arr):
        max_seen, total = 0, 0
        for i, v in enumerate(arr, 1):
            max_seen = max(max_seen, v)
            if max_seen == i - 1:
                total += 1
        return total
