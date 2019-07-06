class Solution(object):
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        dp = [nums[0]] * len(nums)
        dp[1] = max(nums[0], nums[1])
        for idx in range(2, len(nums) - 1):
            dp[idx] = max(dp[idx - 2] + nums[idx], dp[idx - 1])
        withoutLast = dp[-2]
        dp[1] = nums[1]
        dp[2] = max(nums[1], nums[2])
        for idx in range(3, len(nums)):
            dp[idx] = max(dp[idx - 2] + nums[idx], dp[idx - 1])
        withoutFirst = dp[-1]
        return max(withoutLast, withoutFirst)
