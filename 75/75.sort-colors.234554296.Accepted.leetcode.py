class Solution(object):
    def sortColors(self, nums):

        start, end = 0, len(nums) - 1
        index = 0
        while start <= end:
            while nums[end] == 2 and end >= 0:
                end -= 1
            if nums[start] == 2 and start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
            if nums[start] == 0:
                nums[start], nums[index] = nums[index], nums[start]
                index += 1
            start += 1
