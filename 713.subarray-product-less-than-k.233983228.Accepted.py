








class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):

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
