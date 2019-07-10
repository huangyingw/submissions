


class Solution(object):
    def findUnsortedSubarray(self, nums):

        minimum = float('inf')
        maximum = -float('inf')
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                minimum = min(nums[i], minimum)
                maximum = max(nums[i - 1], maximum)
        if minimum == float('inf'):
            return 0
        for i in range(len(nums)):
            if nums[i] > minimum:
                left = i
                break
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < maximum:
                right = i
                break
        return right - left + 1
