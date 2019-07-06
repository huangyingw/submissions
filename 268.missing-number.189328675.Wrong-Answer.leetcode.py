class Solution(object):
    def missingNumber(self, nums):
        for num in nums:
            if num < len(nums):
                nums[num] = num
        missing = len(nums)
        for idx in range(len(nums)):
            if nums[idx] != idx:
                missing = idx
        return missing
