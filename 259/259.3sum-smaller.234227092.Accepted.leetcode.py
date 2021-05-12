class Solution(object):
    def threeSumSmaller(self, nums, target):
        nums.sort()
        ls = len(nums)
        res = 0
        for i in range(ls - 1):
            res += self.twoSumSmaller(nums, i + 1, target - nums[i])
        return res

    def twoSumSmaller(self, nums, start, target):
        res, left, right = 0, start, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                res += right - left
                left += 1
            else:
                right -= 1
        return res
