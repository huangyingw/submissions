class Solution(object):
    def canReach(self, arr, start):
        n = len(arr)
        visited = set()

        def helper(i):
            if i < 0 or i >= n:
                return False
            if arr[i] == 0:
                return True
            if i in visited:
                return False
            visited.add(i)
            return helper(i + arr[i]) or helper(i - arr[i])
        return helper(start)
