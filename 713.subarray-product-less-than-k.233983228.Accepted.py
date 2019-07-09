_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        subarrays = 0
        start = 0
        product = 1
        for end, num in enumerate(nums):
            product *= num
            while product >= k and start <= end:
                product //= nums[start]
                start += 1
            subarrays += end - start + 1
        return subarrays
