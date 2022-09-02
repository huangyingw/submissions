class Solution(object):
    def longestSubarray(self, nums, limit):
        start = end = 0
        vmax, vmin = nums[end], nums[start]
