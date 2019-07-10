class Solution(object):
    def findMaxAverage(self, nums, k):
        window_sum = sum(nums[:k])
        max_average = window_sum / float(k)
        for i in range(len(nums) - k):
            window_sum += nums[i + k] - nums[i]
            max_average = max(max_average, window_sum / float(k))
        return max_average
