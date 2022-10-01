class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        last_seen = {}
        start = 0
        vmax = 0
        for i, c in enumerate(nums):
            if c in last_seen:
                start = max(start, last_seen[c] + 1)
                vmax = nums[start]
            vmax += c
            last_seen[c] = i
        return vmax
