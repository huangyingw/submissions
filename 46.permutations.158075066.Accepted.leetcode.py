class Solution(object):
    def permute(self, nums):
        def dfs():
            for index in range(len(nums)):
                if len(current) == len(nums):
                    result.append(list(current))
                    return
                if nums[index] not in current:
                    current.append(nums[index])
                    dfs()
                    current.pop()
        current = []
        result = []
        dfs()
        return result
