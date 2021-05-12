class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []
        end = nums[0]
        start = end
        result = []
        for idx in range(len(nums)):
            if nums[idx] == nums[idx + 1]:
                continue
            start = end
            end = nums[idx]
            result.append(str(start) if start == end else str(start) + '->' + str(end))
        return result
