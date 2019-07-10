class Solution(object):
    def subsets(self, nums):

        def helper(start):
            for index in range(start, len(nums)):
                current.append(nums[start])
                result.append(list(current))
                helper(start + 1)
                current.pop()
        result = []
        current = []
        nums.sort()
        helper(0)
        return result
