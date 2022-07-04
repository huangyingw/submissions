class Solution(object):
    def canJump(self, nums):

        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False

        maxNum = max(nums)

        for i in range(nums.count(0)):
            index = nums.index(0)

            if index == len(nums) - 1:
                return True
            j = 1
            jump = False

            while(j <= maxNum and index - j >= 0):
                if nums[index - j] > j:
                    j += maxNum
                    jump = True
                j += 1
            if jump is False:
                return False
            else:
                nums[index] = -1
        return True
