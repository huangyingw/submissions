class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        deq = []
        result = []
        for idx, val in enumerate(nums):
            while deq and nums[deq[-1]] < val:
                deq.pop()
            deq.append(idx)
            while deq and idx - deq[0] + 1 > k:
                deq.pop(0)
            if idx + 1 >= k:
                result.append(nums[deq[0]])
        return result
