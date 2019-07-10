class Solution:
    def maxSubArrayLen(self, nums, k):
        sum, ret = 0, 0
        map = {}
        for i in range(len(nums)):
            sum += nums[i]
            if sum == k:
                ret = i + 1
            elif sum - k in map:
                ret = max(i - map[sum - k], ret)
            if sum not in map:
                map[sum] = i
        return ret
