class Solution(object):
    def search(self, nums, target):

        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            if nums[r] >= nums[m]:
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
