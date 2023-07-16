class Solution(object):
    def sortColors(self, nums):

        index0, index1 = 0, 0
        for i in range(0, len(nums)):
            v = nums[i]
            nums[i] = 2
            if v == 0:
                nums[index1] = 1
                index1 += 1
                nums[index0] = 0
                index0 += 1
            elif v == 1:
                nums[index1] = 1
                index1 += 1
