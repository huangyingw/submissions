








class Solution(object):
    def removeElement(self, nums, val):

        next_free = 0
        for i, num in enumerate(nums):
            if num != val:
                nums[next_free] = num
                next_free += 1
        return next_free
