class Solution(object):
    def missingNumber(self, nums):
        for num in nums:
            if num < len(nums):
                nums[num] = num
        missing = len(nums)
        for num in nums:
            if num < len(nums) and nums[num] != num:
                missing = num
        return missing
