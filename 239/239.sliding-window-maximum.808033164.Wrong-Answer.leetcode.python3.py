class Solution(object):
    def maxSlidingWindow(self, nums, k):
        dequeue = []
        result = []
        for idx in range(len(nums)):
            while dequeue and nums[dequeue[-1]] < nums[idx]:
                dequeue.pop()
            dequeue += [idx]
            if dequeue[-1] - dequeue[0] + 1 > k:
                dequeue.pop(0)
            result += [nums[dequeue[0]]]
        return result
