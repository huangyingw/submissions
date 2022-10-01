class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        last_seen = {}
        result = vsum = start = 0
        for i, c in enumerate(nums):
            if c in last_seen:
                old_start = start
                start = max(start, last_seen[c] + 1)
                for idx in range(old_start, start):
                    vsum -= nums[idx]
                vsum += nums[start]
            vsum += c
            result = max(result, vsum)
            last_seen[c] = i
        return vmax
