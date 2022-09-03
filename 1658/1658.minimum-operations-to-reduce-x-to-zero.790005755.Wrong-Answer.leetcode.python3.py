class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        vsum = sum(nums)
        current = start = 0
        target = vsum - x
        maxLen = 0
        for idx, val in enumerate(nums):
            current += val
            while current > target:
                current -= nums[start]
                start += 1
            maxLen = max(maxLen, idx - start + 1)
        return len(nums) - maxLen
