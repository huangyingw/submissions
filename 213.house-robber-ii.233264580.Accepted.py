













class Solution(object):
    def rob(self, nums):

        if len(nums) < 2:
            return sum(nums)
        loot, prev = 0, 0
        for num in nums[1:]:
            loot, prev = max(num + prev, loot), loot
        nums[-1] = 0
        loot2, prev = 0, 0
        for num in nums:
            loot2, prev = max(num + prev, loot2), loot2
        return max(loot, loot2)
