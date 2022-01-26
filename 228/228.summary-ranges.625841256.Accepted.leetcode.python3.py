class Solution(object):
    def summaryRanges(self, nums):
        start = 0
        result = []
        for idx in range(1, len(nums) + 1):
            if idx < len(nums) and nums[idx - 1] + 1 == nums[idx]:
                continue
            end = idx - 1
            result.append(str(nums[start]) if start == end else str(nums[start]) + '->' + str(nums[end]))
            start = idx
        return result
