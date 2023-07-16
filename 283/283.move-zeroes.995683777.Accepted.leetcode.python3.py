class Solution:
    def moveZeroes(self, nums):
        left = 0
        for idx in range(len(nums)):
            if nums[idx] != 0:
                if idx != left:
                    nums[idx], nums[left] = nums[left], nums[idx]
                left += 1
