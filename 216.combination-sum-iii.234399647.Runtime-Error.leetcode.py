class Solution1:
    def combinationSum3(self, k, n):
        from itertools import combinations
        return [com for com in combinations(range(1, 10), k) if sum(com) == n]
class Solution2:
    def combinationSum3(self, k, n):
        res = []
        re = []
        def dfs(curr, target):
            if len(re) == k:
                if target == 0:
                    res.append(list(re))
                return
            if curr == 10:
                return
            for i in range(curr, 10):
                if target - i < 0:
                    break
                re.append(i)
                dfs(i + 1, target - i)
                re.remove(i)
        dfs(1, n)
        return res
    t = Solution1()
