class Solution(object):
    def combine(self, n, k):
        def dfs(left, right, k):
            if k == 0:
                result.append(list(current))
            for index in range(left, right + 1):
                current.append(index)
                dfs(index + 1, right, k - 1)
                current.pop()
        current = []
        result = []
        dfs(1, n, k)
        return result
