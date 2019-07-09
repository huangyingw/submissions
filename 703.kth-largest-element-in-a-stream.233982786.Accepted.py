_author_ = 'jake'
_project_ = 'leetcode'











import heapq


class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        self.k = k
        self.nums = nums

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.nums) == self.k and val <= self.nums[0]:
            return self.nums[0]
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
