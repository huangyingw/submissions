class Solution:
    def removeDuplicates1(self, nums):
        i = 0
        for n in nums:
            if i < 2 or n > nums[i - 2]:
                nums[i] = n
                i += 1
        return i
    def removeDuplicates2(self, nums):
        i = 2
        while (i < len(nums)):
            if nums[i] == nums[i - 1] == nums[i - 2]:
                nums.remove(nums[i])
            else:
                i += 1
        return len(nums)
