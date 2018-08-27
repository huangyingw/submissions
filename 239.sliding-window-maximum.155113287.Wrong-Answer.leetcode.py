class Solution(object):
    def maxSlidingWindow(self, nums, k):
        dequeue = []
        result = []

        for idx, val in enumerate(nums):
            while dequeue and nums[dequeue[-1]] < val:
                dequeue.pop()

            dequeue.append(idx)

            while dequeue and idx - dequeue[0] + 1 > k:
                dequeue.pop(0)

            if idx + 1 >= k:
                result.append(dequeue[0])

        return result
