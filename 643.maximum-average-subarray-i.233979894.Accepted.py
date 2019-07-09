_author_ = 'jake'
_project_ = 'leetcode'








class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window_sum = sum(nums[:k])
        max_average = window_sum / float(k)
        for i in range(len(nums) - k):
            window_sum += nums[i + k] - nums[i]
            max_average = max(max_average, window_sum / float(k))
        return max_average
