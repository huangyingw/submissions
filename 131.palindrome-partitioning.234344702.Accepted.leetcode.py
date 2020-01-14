class Solution:
    def partition(self, s):
        res = []
        self.dfs(res, [], s)
        return res
    def dfs(self, res, path, s):
        if not s:
            res.append(path[:])
            return
        for i in range(1, len(s) + 1):
            if s[:i] == s[i - 1::-1]:
                self.dfs(res, path + [s[:i]], s[i:])
