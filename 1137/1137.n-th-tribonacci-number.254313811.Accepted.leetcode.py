class Solution(object):
    def tribonacci(self, n):
        nums = [0, 1, 1]
        while len(nums) <= n:
            nums.append(sum(nums[-3:]))
        return nums[n]
