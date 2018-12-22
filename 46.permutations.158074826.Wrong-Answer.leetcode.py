class Solution(object):
    def permute(self, nums):
        def dfs():
            for index in range(len(nums)):
                if len(current) == len(nums):
                    result.append(list(current))

                if not visited[index]:
                    visited[index] = True
                    current.append(nums[index])
                    print("current.append --> %s\n" % current)
                    dfs()
                    current.pop()
                    print("current.append --> %s\n" % current)
                    visited[index] = False

        visited = [False for _ in range(len(nums))]
        current = []
        result = []
        dfs()
        return result
