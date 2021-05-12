class Solution(object):
    def moveZeroes(self, nums):
        k = 0
        for num in nums:
            if num != 0:
                nums[k] = num
                k += 1
        nums[k:] = [0] * (len(nums) - k)
