class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []
        start = nums[0]
        result = []
        for idx in range(1, len(nums)):
            if nums[idx - 1] + 1 == nums[idx]:
                end = nums[idx]
                continue
            result.append(str(start) if start == end else str(start) + '->' + str(end))
            start = nums[idx]
            end = nums[idx]
        result.append(str(start) if start == end else str(start) + '->' + str(end))
        return result
