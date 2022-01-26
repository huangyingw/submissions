class Solution(object):
    def summaryRanges(self, nums):
        start = end = 0
        result = []
        for idx in range(len(nums)):
            if idx + 1 < len(nums) and nums[idx] + 1 == nums[idx + 1]:
                continue
            end = idx
            result.append(str(nums[start]) if start == end else str(nums[start]) + '->' + str(nums[end]))
            start = end + 1
        return result
