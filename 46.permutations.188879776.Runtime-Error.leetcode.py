class Solution(object):
    def permute(self, nums):
        def dfs():
            for index in range(len(nums)):
                if len(current) == len(nums):
                    result.add(list(current))
                if not visited[index]:
                    visited[index] = True
                    current.append(nums[index])
                    dfs()
                    current.pop()
                    visited[index] = False
        nums.sort()
        visited = [False for _ in range(len(nums))]
        current = []
        result = set()
        dfs()
        return result
