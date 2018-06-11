class Solution(object):
    def permute(self, nums):
        def helper():
            for index in range(len(nums)):
                if len(current) == len(nums):
                    result.append(list(current))

                if not visited[index]:
                    visited[index] = True
                    current.append(nums[index])
                    helper()
                    current.pop()
                    visited[index] = False

        visited = [False for _ in range(len(nums))]
        current = []
        result = []
        helper()
        return result
