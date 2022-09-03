class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        vsum = sum(nums)
        current = start = 0
        target = vsum - x
        maxLen = 0
        for idx, val in enumerate(nums):
            current += val
            while start < idx and current > target:
                current -= nums[start]
                start += 1
            if current == target:
                maxLen = max(maxLen, idx - start + 1)
        return len(nums) - maxLen if maxLen > 0 else -1
