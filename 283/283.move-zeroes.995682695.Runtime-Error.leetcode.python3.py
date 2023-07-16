class Solution:
    def moveZeroes(self, nums):
        left = 0
        for idx in range(len(nums)):
            if nums[idx] != 0:
                nums[idx], nums[left] = nums[left], nums[idx]
                left += 1
        nums[left:] = 0
