class Solution:
    def canJump(self, nums):

        currentEnd, currentFarthest = 0, 0
        for i in range(len(nums) - 1):
            currentFarthest = max(i + nums[i], currentFarthest)
            if i == currentEnd:
                currentEnd = currentFarthest
            if currentEnd > len(nums) - 1:
                break
        return currentEnd >= len(nums) - 1
