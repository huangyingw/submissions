class Solution(object):
    def subsets(self, nums):
        def dfs(start):
            result.append(list(current))
            for index in range(start, len(nums)):
                current.append(nums[index])
                dfs(index + 1)
                current.pop()

        result = []
        current = []
        dfs(0)
        return result
