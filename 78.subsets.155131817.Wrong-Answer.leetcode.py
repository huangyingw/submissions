class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(start):
            result.append(list(current))
            for index in range(start, len(nums)):
                current.append(nums[start])
                dfs(index + 1)
                current.pop()

        result = []
        current = []
        nums.sort()
        dfs(0)
        return result
