class Solution(object):
    def removeDuplicates(self, nums):

        index = 1
        for num in nums:
            if nums[index - 1] != num:
                nums[index] = num
                index += 1
        return index
