_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def minSubArrayLen(self, s, nums):

        subarray_sum, min_length, start = 0, len(nums) + 1, 0
        for i in range(len(nums)):
            subarray_sum += nums[i]
            while subarray_sum >= s:
                min_length = min(min_length, i - start + 1)
                subarray_sum -= nums[start]
                start += 1
        return 0 if min_length > len(nums) else min_length
