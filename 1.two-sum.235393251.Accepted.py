class Solution:
    def twoSum(self, nums, target):

        n = 0
        while(n != len(nums)):
            z = target - nums[n]
            try:
                return n, nums.index(z, n + 1)
            except:
                pass
            n += 1
