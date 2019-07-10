_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def maxSubArrayLen(self, nums, k):

        cumul, max_length = 0, 0
        first_index = {}
        for i, num in enumerate(nums):
            cumul += num
            if cumul == k:
                max_length = i + 1
            elif cumul - k in first_index:
                max_length = max(max_length, i - first_index[cumul - k])
            if cumul not in first_index:
                first_index[cumul] = i
        return max_length
