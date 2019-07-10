class Solution(object):
    def rob(self, nums):
        l = len(nums)
        if l == 0:
            return 0
        elif l == 1:
            return nums[0]
        prev2, prev1 = nums[0], max(nums[0], nums[1])
        for i in range(2, l):
            curr = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = curr
        return prev1
