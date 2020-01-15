import heapq


class Solution(object):
    def maxNumberOfApples(self, arr):
        capacity = 5000
        apples = 0
        heapq.heapify(arr)
        while arr and capacity - arr[0] >= 0:
            capacity -= heapq.heappop(arr)
            apples += 1
        return apples
