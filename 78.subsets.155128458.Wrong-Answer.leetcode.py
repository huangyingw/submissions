class Solution(object):
    def subsets(self, nums):
        def dfs(start):
            for index in range(start, len(nums)):
                current.append(nums[start])
                result.append(list(current))
                dfs(start + 1)
                current.pop()
        result = []
        current = []
        nums.sort()
        dfs(0)
        return result
