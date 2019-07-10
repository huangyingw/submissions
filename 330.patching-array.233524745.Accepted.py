










class Solution(object):
    def minPatches(self, nums, n):

        next_missing = 1
        patches = 0
        i = 0
        while next_missing <= n:
            if i < len(nums) and nums[i] <= next_missing:
                next_missing += nums[i]
                i += 1
            else:
                next_missing += next_missing
                patches += 1
        return patches
