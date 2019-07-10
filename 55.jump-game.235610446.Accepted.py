class Solution:
    def canJump(self, nums):
        for i in range(0, len(nums) - 1):
            if nums[i] == 0:
                for x in range(i - 1, -2, -1):
                    if (x < 0):
                        return False
                    elif (nums[x] > (i - x)):
                        break
        return True
