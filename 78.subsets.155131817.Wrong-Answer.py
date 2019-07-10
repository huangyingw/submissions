class Solution(object):
    def subsets(self, nums):

        def helper(start):
            result.append(list(current))
            for index in range(start, len(nums)):
                current.append(nums[start])
                helper(index + 1)
                current.pop()
        result = []
        current = []
        nums.sort()
        helper(0)
        return result
