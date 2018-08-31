class Solution(object):
    def maxSlidingWindow(self, nums, k):
        deq = []
        result = []

        for idx, val in enumerate(nums):
            while deq and nums[deq[-1]] < val:
                deq.pop()

            deq.append(idx)

            if idx + 1 < k:
                continue

            while deq and idx - deq[0] + 1 > k:
                deq.pop(0)

            result.append(nums[deq[0]])

        return result
