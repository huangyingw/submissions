


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        import heapq
        for num in nums:
            heapq.heappush(heap, -(num))
        result = 0
        for _ in range(k):
            result = heapq.heappop(heap)
        return -(result)
