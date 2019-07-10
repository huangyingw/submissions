


class Solution:
    def dominantIndex(self, nums):

        big = secondBig = index = -1
        for i in range(len(nums)):
            if nums[i] > big:
                big, secondBig = nums[i], big
                index = i
            elif nums[i] > secondBig:
                secondBig = nums[i]
        if big >= secondBig * 2:
            return index
        return -1
