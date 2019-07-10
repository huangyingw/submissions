class Solution(object):
    def subsetsWithDup(self, nums):

        def dfs(start):
            result.append(list(current))
            for index in range(start, len(nums)):
                if index > start and nums[index] == nums[index - 1]:
                    continue
                current.append(nums[index])
                dfs(index + 1)
                current.pop()
        nums.sort()
        result = []
        current = []
        dfs(0)
        return result
