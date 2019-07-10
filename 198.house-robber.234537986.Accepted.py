
class Solution:

    def rob(self, nums):

        if not nums:
            return 0
        memo = [0 for _ in range(len(nums) + 1)]
        memo[1] = nums[0]
        for i in range(1, len(nums)):
            memo[i + 1] = max(memo[i], memo[i - 1] + nums[i])
        return memo[len(nums)]


    def rob(self, nums):


        if not nums:
            return 0
        pre1 = 0
        pre2 = 0
        i = 0
        for num in nums:
            temp = pre1
            pre1 = max(pre2 + num, pre1)
            pre2 = temp
        return pre1
