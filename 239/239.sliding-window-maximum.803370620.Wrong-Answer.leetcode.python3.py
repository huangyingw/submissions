class Solution(object):
    def maxSlidingWindow(self, nums, k):
        dequeue = []
        result = []
        for idx, val in enumerate(nums):
            if dequeue and nums[dequeue[-1]] < val:
                dequeue.pop()
            dequeue.append(idx)
            if idx + 1 < k:
                continue
            if idx - dequeue[0] + 1 > k:
                dequeue.pop(0)
            result.append(nums[dequeue[0]])
        return result
