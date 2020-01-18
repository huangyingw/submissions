class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        result, min_diff = 0, float('inf')
        for index in range(len(nums) - 1):
            left = index + 1
